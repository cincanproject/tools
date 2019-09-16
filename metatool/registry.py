import docker
import docker.errors
import logging
import pathlib
import requests
import json
import datetime
from typing import List, Set, Dict, Tuple, Optional, Any, Iterable


class ToolInfo:
    """A tool in registry"""
    def __init__(self, name: str, updated: datetime.datetime, input: List[str] = None, output: List[str] = None,
                 tags: List[str] = '', description: str = ''):
        self.name = name
        self.updated = updated
        self.input = input if input is not None else []
        self.output = output if output is not None else []
        self.tags = tags
        self.description = description

    def __str__(self):
        return "{} {}".format(self.name, self.description)


def parse_json_time(string: str) -> datetime.datetime:
    """Parse time from JSON as stored by Docker"""
    s = string[0: 19]
    return datetime.datetime.strptime(s, '%Y-%m-%dT%H:%M:%S')


def format_time(time: datetime.datetime) -> str:
    """Format time as we would like to see it"""
    return time.strftime('%Y-%m-%dT%H:%M:%S')


def tools_to_json(tools: Iterable[ToolInfo]) -> Dict[str, Any]:
    """Write tool info into JSON format"""
    r = {}
    for t in tools:
        td = {'updated': format_time(t.updated)}
        if t.description != '':
            td['description'] = t.description
        if len(t.input) > 0:
            td['input'] = t.input
        if len(t.output) > 0:
            td['output'] = t.output
        if len(t.tags) > 0:
            td['tags'] = ','.join(t.tags)  # keep order
        r[t.name] = td
    return r


def parse_data_types(string: str) -> List[str]:
    """Parse list of data types into a list"""
    s = string.strip()
    if len(s) == 0:
        return []
    return list(map(lambda x: x.strip(), s.split(',')))


def split_tool_tag(tag: str) -> (str, str):
    """Split tool tag into tool name and tool version"""
    tag_split = tag.split(':', maxsplit=2)
    return tag_split[0], tag_split[1] if len(tag_split) > 1 else 'latest'


class ToolRegistry:
    """A tool registry"""
    def __init__(self):
        self.logger = logging.getLogger('registry')
        self.client = docker.from_env()
        self.tool_cache = pathlib.Path.home() / '.cincan' / 'tools.json'
        self.hub_url = "https://hub.docker.com/v2"
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
                self.logger.debug("using remote image for %s", use_tools[i].name)
            elif i not in remote_tools:
                use_tools[i] = local_tools[i]
                self.logger.debug("using local image for %s", use_tools[i].name)
            else:
                local = local_tools[i]
                remote = remote_tools[i]
                if local.updated >= remote.updated:
                    use_tools[i] = local
                    self.logger.debug("using local image for %s", use_tools[i].name)
                else:
                    use_tools[i] = remote
                    self.logger.debug("using remote image for %s", use_tools[i].name)
                # assume all unique local tags are newer than remote ones
                use_tags = [i for i in local.tags if i not in remote.tags] + remote.tags
                use_tools[i].tags = use_tags
                # description only in registry, not locally
                use_tools[i].description = remote_tools[i].description
        return use_tools

    def list_tools_local_images(self) -> Dict[str, ToolInfo]:
        """List tools from the locally available docker images"""
        images = self.client.images.list(filters={'label': 'io.cincan.input'})
        # images oldest first (tags are listed in proper order)
        images.sort(key=lambda x: parse_json_time(x.attrs['Created']), reverse=True)
        ret = {}
        for i in images:
            if len(i.tags) == 0:
                continue  # not sure what these are...
            name, tag = split_tool_tag(i.tags[0])
            updated = parse_json_time(i.attrs['Created'])
            input = parse_data_types(i.labels.get('io.cincan.input', ''))
            output = parse_data_types(i.labels.get('io.cincan.output', ''))
            if name in ret:
                ret[name].tags.append(tag)
            else:
                ret[name] = ToolInfo(name, updated, list(input), list(output), tags=[tag])
                self.logger.debug("%s input: %s output: %s", name, input, output)
        return ret

    def fetch_remote_data(self, tool: ToolInfo) -> Dict[str, Any]:
        """Fetch remote data to update a tool info"""
        self.logger.info("fetch %s...", tool.name)
        manifest = self.fetch_manifest(tool.name)
        v1_comp_string = manifest.get('history', [{}])[0].get('v1Compatibility')
        if v1_comp_string is None:
            return {}
        v1_comp = json.loads(v1_comp_string)
        labels = v1_comp['container_config']['Labels']
        if labels:
            tool.input = parse_data_types(labels.get('io.cincan.input', ''))
            tool.output = parse_data_types(labels.get('io.cincan.output', ''))
        tool.tags = manifest.get('sorted_tags', None)  # Note: not part of manifest in Docker API
        return manifest

    def fetch_manifest(self, tool_tag: str) -> Dict[str, Any]:
        """Fetch docker image tag and manifest information"""
        tool_name, tool_version = split_tool_tag(tool_tag)

        # Get tags for the tool
        tags_req = requests.get(self.hub_url + "/repositories/" + tool_name + "/tags?page_size=1000")
        if tags_req.status_code != 200:
            self.logger.error(
                "Error getting tags for tool {}, code: {}".format(tool_name, tags_req.status_code))
            return {}
        tags = json.loads(tags_req.content)
        # sort tags by update time
        tags_sorted = sorted(tags.get('results', []), key=lambda x: parse_json_time(x['last_updated']), reverse=True)
        tag_names = list(map(lambda x: x['name'], tags_sorted))
        if tool_tag.count(':') == 0 and tag_names:
            tool_version = tag_names[0]  # tool version not given, pick newest

        # Get bearer token for the image
        token_req = requests.get(self.auth_url + "?service=registry.docker.io&scope=repository:"
                                 + tool_name + ':pull')
        if token_req.status_code != 200:
            self.logger.error("Error getting token for tool {}, code: {}".format(tool_name, token_req.status_code))
            return {}
        token_json = json.loads(token_req.content)
        token = token_json['token']

        # Get manifest of the image
        # Note, must not request 'v2' metadata as that does not contain what is now in 'v1Compatibility' :O
        manifest_req = requests.get(self.registry_url + "/" + tool_name + "/manifests/" + tool_version,
                                    headers={'Authorization': ('Bearer ' + token),
                                             # 'Accept': 'application/vnd.docker.distribution.manifest.v2+json',
                                             })
        if manifest_req.status_code != 200:
            self.logger.error(
                "Error getting manifest for tool {}, code: {}".format(tool_name, manifest_req.status_code))
            return {}
        manifest = json.loads(manifest_req.content)

        manifest['all_tags'] = tags  # adding tags to manifest data
        manifest['sorted_tags'] = tag_names
        return manifest

        # curl -s "https://registry.hub.docker.com/v2/repositories/cincan/"
        # curl https://hub.docker.com/v2/repositories/cincan/tshark/tags
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
                    self.fetch_remote_data(t)
                    updated += 1
                else:
                    tool_list[t.name] = old_tools[t.name]
                    self.logger.debug("no updates for %s", t.name)
            # save the tool list
            if updated > 0:
                self.tool_cache.parent.mkdir(parents=True, exist_ok=True)
                with self.tool_cache.open("w") as f:
                    self.logger.debug("saving tool cache %s", self.tool_cache)
                    json.dump(tools_to_json(tool_list.values()), f)
        # read saved tools and return
        return self.read_tool_cache()

    def read_tool_cache(self) -> Dict[str, ToolInfo]:
        """Read the local tool cache file"""
        if not self.tool_cache.exists():
            return {}
        r = {}
        with self.tool_cache.open("r") as f:
            root_json = json.load(f)
            for name, j in root_json.items():
                r[name] = ToolInfo(name, updated=parse_json_time(j['updated']),
                                   input=j.get('input', []), output=j.get('output'),
                                   tags=j.get('tags', '').split(','), description=j.get('description', ''))
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

