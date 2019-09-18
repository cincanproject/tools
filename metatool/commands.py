from typing import List, Set, Dict, Tuple, Optional, Any


class ToolCommands:
    """Tool commands and options"""
    def __init__(self, json: List[Dict[str,Any]]):
        self.json = json

    def command_hints(self) -> List[str]:
        lines = []
        for c in self.json:
            c_str = " ".join(c['command'])
            lines.append(c_str.replace("<file>", "^<file>"))
        return lines
