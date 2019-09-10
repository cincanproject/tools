import docker
import docker.errors
import logging
import pathlib
import requests
import json
import datetime
import re
from typing import List, Set, Dict, Tuple, Optional, Any, Iterable


class ToolInfo:
    """A tool in registry"""
    def __init__(self, name: str, updated: datetime.datetime, input: List[str] = None, output: List[str] = None,
                 description: str = ''):
        self.name = name
        self.updated = updated
        self.input = input if input is not None else []
        self.output = output if output is not None else []
        self.description = description

    def __str__(self):
        return "{}\t{} =>\t {}".format(self.name, self.input, self.output)


def parse_json_time(string: str) -> datetime.datetime:
    s = string[0: 19]
    return datetime.datetime.strptime(s, '%Y-%m-%dT%H:%M:%S')


def tools_to_json(tools: Iterable[ToolInfo]) -> Dict[str, Any]:
    r = {}
    for t in tools:
        td = {'updated': t.updated.strftime('%Y-%m-%dT%H:%M:%S')}
        if t.description != '':
            td['description'] = t.description
        if len(t.input) > 0:
            td['input'] = t.input
        if len(t.output) > 0:
            td['output'] = t.output
        r[t.name] = td
    return r


def parse_data_types(string: str) -> List[str]:
    s = string.strip()
    if len(s) == 0:
        return []
    return list(map(lambda x: x.strip(), s.split(',')))


def split_tool_tag(tag: str) -> (str, str):
    tag_split = tag.split(':', maxsplit=2)
    return tag_split[0], tag_split[1] if len(tag_split) > 1 else 'latest'


class ToolRegistry:
    """A tool registy"""
    def __init__(self):
        self.logger = logging.getLogger('registry')
        self.client = docker.from_env()
        self.tool_cache = pathlib.Path.home() / '.cincan' / 'tools.json'
        self.auth_url = "https://auth.docker.io/token"
        self.registry_url = "https://registry.hub.docker.com/v2"

    def list_tools(self) -> Dict[str, ToolInfo]:
        """List all tools"""
        local_tools = self.list_tools_local_images()
        remote_tools = self.list_tools_registry()
        use_tools = {}
        for i in set().union(local_tools.keys(), remote_tools.keys()):
            if i not in local_tools:
                use_tools[i] = remote_tools[i]
            elif i not in remote_tools:
                use_tools[i] = local_tools[i]
            else:
                local = local_tools[i]
                remote = remote_tools[i]
                use_tools[i] = local if local.updated >= remote.updated else remote
                use_tools[i].description = remote_tools[i].description  # description only in registry, not locally
        return use_tools

    def list_tools_local_images(self) -> Dict[str, ToolInfo]:
        """List tools from the locally available docker images"""
        images = self.client.images.list(filters={'label': 'io.cincan.input'})
        ret = {}
        for i in images:
            if len(i.tags) == 0:
                continue  # not sure what these are...
            name = i.tags[0].replace(':latest', '')
            updated = parse_json_time(i.attrs['Created'])
            input = parse_data_types(i.labels.get('io.cincan.input', ''))
            output = parse_data_types(i.labels.get('io.cincan.output', ''))
            self.logger.debug("%s input: %s output: %s", name, input, output)
            ret[name] = ToolInfo(name, updated, list(input), list(output))
        return ret

        # Local cache file in
        # ~/.cincan/commands/<name>.json

    def fetch_remote_labels(self, tool: ToolInfo) -> Dict[str,Any]:
        self.logger.info("updating %s...", tool.name)
        manifest = self.fetch_manifest(tool.name)
        v1_comp_string = manifest.get('history', [{}])[0].get('v1Compatibility')
        if v1_comp_string is None:
            return {}
        v1_comp = json.loads(v1_comp_string)
        labels = v1_comp['container_config']['Labels']
        if labels:
            tool.input = parse_data_types(labels.get('io.cincan.input', ''))
            tool.output = parse_data_types(labels.get('io.cincan.output', ''))
        return manifest

    def fetch_manifest(self, tool_tag: str) -> Dict[str, Any]:
        tool_name, tool_version = split_tool_tag(tool_tag)
        token_req = requests.get(self.auth_url + "?service=registry.docker.io&scope=repository:"
                                 + tool_name + ':pull')
        if token_req.status_code != 200:
            self.logger.error("Error getting token for tool {}, code: {}".format(tool_name, token_req.status_code))
            return {}
        token_json = json.loads(token_req.content)
        token = token_json['token']
        # Note, must not request 'v2' metadata as that does not contain what is now in 'v1Compatibility' :O
        manifest_req = requests.get(self.registry_url + "/" + tool_name + "/manifests/" + tool_version,
                                    headers={'Authorization': ('Bearer ' + token),
                                             # 'Accept': 'application/vnd.docker.distribution.manifest.v2+json',
                                             })
        if manifest_req.status_code != 200:
            self.logger.error(
                "Error getting token for tool {}, code: {}".format(tool_name, manifest_req.status_code))
            return {}
        manifest = json.loads(manifest_req.content)
        return manifest

        # curl -s "https://registry.hub.docker.com/v2/repositories/cincan/"
        # curl - sSL "https://auth.docker.io/token?service=registry.docker.io&scope=repository:raulik/test-test-tool:pull" | jq - r.token > bearer - token
        # curl - s H "Authorization: Bearer `cat bearer-token`" "https://registry.hub.docker.com/v2/raulik/test-test-tool/manifests/latest" | python - m json.tool

    def list_tools_registry(self) -> Dict[str, ToolInfo]:
        """List tools from registry with help of local cache"""
        # Get fresh list of tools from remote registry
        fresh_resp = requests.get(self.registry_url + "/repositories/cincan/?page_size=1000")
        if fresh_resp.status_code != 200:
            self.logger.error("Error getting list of remote tools, code: {}".format(fresh_resp.status_code))
        else:
            # get a images JSON, form new tool list
            fresh_json = json.loads(fresh_resp.content)
            tool_list = {}
            for t in fresh_json['results']:
                name = "{}/{}".format(t['user'], t['name'])
                tool_list[name] = ToolInfo(name, updated=parse_json_time(t['last_updated']),
                                           description=t.get('description', ''))
            # update tool info, when required
            old_tools = self.read_tool_cache()
            updated = 0
            for t in tool_list.values():
                if t.name not in old_tools or t.updated > old_tools[t.name].updated:
                    self.fetch_remote_labels(t)
                    updated += 1
                else:
                    tool_list[t.name] = old_tools[t.name]
                    self.logger.info("no updates for %s", t.name)
            # save the tool list
            if updated > 0:
                self.tool_cache.parent.mkdir(parents=True, exist_ok=True)
                with self.tool_cache.open("w") as f:
                    self.logger.debug("saving tool cache %s", self.tool_cache)
                    json.dump(tools_to_json(tool_list.values()), f)
        # read saved tools and return
        return self.read_tool_cache()

    def read_tool_cache(self) -> Dict[str, ToolInfo]:
        if not self.tool_cache.exists():
            return {}
        r = {}
        with self.tool_cache.open("r") as f:
            root_json = json.load(f)
            for name, j in root_json.items():
                r[name] = ToolInfo(name, updated=parse_json_time(j['updated']),
                                   input=j.get('input', []), output=j.get('output'),
                                   description=j.get('description', ''))
        return r


        # TheHive accepts the following datatypes:
        # domain
        # file
        # filename
        # fqdn
        # hash
        # ip
        # mail
        # mail_subject
        # other
        # regexp
        # registry
        # uri_path
        # url
        # user-agent

