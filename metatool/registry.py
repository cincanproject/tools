import docker
import docker.errors
import logging
import pathlib
import requests
import json
import datetime
from typing import List, Set, Dict, Tuple, Optional, Any


class ToolInfo:
    """A tool in registry"""
    def __init__(self, name: str, updated: datetime.datetime, input: List[str] = None, output: List[str] = None):
        self.name = name
        self.updated = updated
        self.input = input if input is not None else []
        self.output = output if output is not None else []

    def __str__(self):
        return "{}\t{} =>\t {}".format(self.name, self.input, self.output)


def parse_json_time(string: str) -> datetime.datetime:
    s = string[0: 19]
    return datetime.datetime.strptime(s, '%Y-%m-%dT%H:%M:%S')


class ToolRegistry:
    """A tool registy"""
    def __init__(self):
        self.logger = logging.getLogger('registry')
        self.client = docker.from_env()
        self.cache_dir = pathlib.Path.home() / '.cincan' / 'commands'
        self.auth_url = "https://auth.docker.io/token"
        self.registry_url = "https://registry.hub.docker.com/v2"

    def list_tools(self) -> Dict[str, ToolInfo]:
        """List all tools"""
        tools = self.list_tools_local_images()
        tools.update(self.list_tools_registry())
        return tools

    def list_tools_local_images(self) -> Dict[str, ToolInfo]:
        """List tools from the locally available docker images"""
        images = self.client.images.list(filters={'label': 'io.cincan.input'})
        ret = {}
        for i in images:
            if len(i.tags) == 0:
                continue  # not sure what these are...
            name = i.tags[0].replace(':latest', '')
            updated = parse_json_time(i.attrs['Created'])
            input = i.labels.get('io.cincan.input', 'application/octet-stream')
            output = i.labels.get('io.cincan.output', 'text/plain')
            self.logger.debug("%s input: %s output: %s", name, input, output)
            ret[name] = ToolInfo(name, updated, input, output)
        return ret

        # Local cache file in
        # ~/.cincan/commands/<name>.json

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
            self.cache_dir.mkdir(parents=True, exist_ok=True)
            fresh_json = json.loads(fresh_resp.content)
            cache_file = self.cache_dir / ".cached"
            with cache_file.open("w") as f:
                self.logger.debug("saving cache %s")
                json.dump(fresh_json, f)
            for t in fresh_json['results']:
                print("{}".format(t['name']))  # FIXME
        return {}

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

