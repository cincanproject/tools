import docker
import docker.errors
import logging
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

    def list_tools_registry(self) -> Dict[str, ToolInfo]:
        """List tools from registry with help of local cache"""
        # FIXME
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

