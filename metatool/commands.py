from typing import List, Set, Dict, Tuple, Optional, Any


class ToolCommands:
    """Tool commands and options"""
    def __init__(self, json: Dict[str,Any]):
        self.commands_json = json['commands']
        self.outputs_json = json.get('output-options', [])

    def is_stdout_output_option(self) -> bool:
        for t in self.outputs_json:
            if t.get('stdout', False):
                return True
        return False

    def get_output_to_file_option(self) -> Optional[List[str]]:
        for t in self.outputs_json:
            args = t.get('args', None)
            if args:
                return args
        return None

    def command_line(self, in_file: str, args: List[str] = None,
                     in_type: Optional[str] = None, out_type: Optional[str] = None) -> List[str]:
        """Create actual command line"""
        all_commands = self.commands_json
        match_commands = []
        for c in self.commands_json:
            if '<file>' not in c['command']:
                continue
            if in_type is not None and in_type not in c.get('input'):
                continue
            if out_type is not None and out_type not in c.get('output'):
                continue
            match_commands.append(c)
        if len(match_commands) != 1:
            raise Exception("Single command should match given input/output filter, now:\n{}".format(
                "\n".join(map(lambda x: "{}{}".format(" -i {}".format(x['input']) if 'input' in x else "",
                                                      " -o {}".format(x['output']) if 'output' in x else ""),
                              match_commands))))
        command = match_commands[0]['command']
        true_args = []
        for arg in command:
            if arg == "<file>":
                true_args.append("^{}".format(in_file))
            else:
                true_args.append(arg)
        for arg in args if args is not None else []:
            true_args.append(arg)
        return true_args

    def command_hints(self) -> List[str]:
        lines = []
        stdout_opt = self.is_stdout_output_option()
        output_opt = self.get_output_to_file_option()
        for c in self.commands_json:
            cmds = c['command']
            str = " ".join(cmds).replace("<file>", "^<file>")
            if output_opt:
                opt_str = " ".join(output_opt).replace("<file>", "^^<file>")
                if stdout_opt:
                    opt_str = "[" + opt_str + "]"
                str = opt_str + " " + str
            lines.append(str)
        return lines
