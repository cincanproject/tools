import docker
import docker.errors
import logging
import pathlib
import requests
import json
from typing import List, Set, Dict, Tuple, Optional


class ToolInfo:
    """A tool in registry"""
    def __init__(self, name: str, input: List[str], output: List[str]):
        self.name = name
        self.input = input
        self.output = output
    def __str__(self):
        return "{}\t{} =>\t {}".format(self.name, self.input, self.output)


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
            input = i.labels.get('io.cincan.input', 'application/octet-stream')
            output = i.labels.get('io.cincan.output', 'text/plain')
            self.logger.debug("%s input: %s output: %s", name, input, output)
            ret[name] = ToolInfo(name, input, output)
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
            fresh_json = json.loads(fresh_resp.content)
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

