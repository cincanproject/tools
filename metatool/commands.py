import pathlib
import re

from typing import List, Set, Dict, Tuple, Optional, Any, Iterable


class ToolCommand:
    def __init__(self, args: List[str],
                 in_file: Optional[str] = None, in_type: Optional[str] = None,
                 out_file: Optional[str] = None, out_type: Optional[str] = None):
        self.args = args
        self.in_file = in_file
        self.in_type = in_type
        self.out_file = out_file
        self.out_type = out_type

    def __str__(self) -> str:
        return " ".join(self.args)


class ToolCommands:
    """Tool commands and options"""
    def __init__(self, json: Dict[str,Any]):
        self.commands_json = json.get('commands', [])
        self.outputs_json = json.get('output-options', [])
        self.file_pattern = re.compile("(<[^>]*(file|dir)>)")

    def is_stdout_output_option(self) -> bool:
        return any(map(lambda t: t.get('stdout', False), self.outputs_json))

    def get_output_to_file_option(self) -> Optional[List[str]]:
        for t in self.outputs_json:
            args = t.get('args', None)
            if args:
                return args
        return None

    def command_line(self, in_file: str, args: List[str] = None,
                     in_type: Optional[str] = None, out_type: Optional[str] = None,
                     write_output: Optional[str] = None) -> ToolCommand:
        """Create actual command line"""
        all_commands = self.commands_json
        match_commands = []
        match_in_type = None
        match_out_type = None
        for c in self.commands_json:
            if not any(map(lambda s: self.file_pattern.match(s), c['command'])):
                continue
            if in_type is not None and in_type not in c.get('input'):
                continue
            if out_type is not None and out_type not in c.get('output'):
                continue
            match_commands.append(c)
            match_in_type = c.get('input')
            match_out_type = c.get('output')
        if len(match_commands) != 1:
            raise Exception("Single command should match given input/output filter, now:\n{}".format(
                "\n".join(map(lambda x: "{}{}".format(" -i {}".format(x['input']) if 'input' in x else "",
                                                      " -o {}".format(x['output']) if 'output' in x else ""),
                              match_commands))))
        command = match_commands[0]['command']
        true_args = []
        if write_output:
            write_opt = self.get_output_to_file_option()
            if not write_opt:
                raise Exception("Cannot use the tool, do not know how to make it to write to a file/directory")
            for arg in write_opt:
                true_args.append(self.file_pattern.sub("^^" + write_output, arg))
        for arg in command:
            true_args.append(self.file_pattern.sub("^" + in_file, arg))
        for arg in args if args is not None else []:
            true_args.append(arg)
        return ToolCommand(true_args, in_file=in_file, in_type=match_in_type,
                           out_file=write_output, out_type=match_out_type)

    def parse_command(self, json: Dict[str, Any], root_dir: str, all_files: Iterable[str],
                      write_output: Optional[str] = None) -> List[ToolCommand]:
        files = []
        for f in json.get('files', []):
            f_name = f.get('name', 'stdout')
            dir_prefix = (root_dir + '/' if root_dir != '' else '') + f_name + '/'
            f_type = f.get('type')
            f_files = list(filter(lambda s: s == f_name or s.startswith(dir_prefix), all_files))
            files += map(lambda s: (s, f_type), f_files)
        if not files:
            raise Exception("No matching files for processing")
        commands = []
        many_files = len(files) > 1
        for n, t in files:
            w_out = (pathlib.Path(write_output) / n).as_posix() if many_files else write_output
            cmd = self.command_line(in_file=n, in_type=t, write_output=w_out)
            commands.append(cmd)
        return commands

    def command_hints(self) -> List[str]:
        lines = []
        stdout_opt = self.is_stdout_output_option()
        output_opt = self.get_output_to_file_option()
        for c in self.commands_json:
            cmds = c['command']
            str = self.file_pattern.sub("^\\1", " ".join(cmds))
            if output_opt:
                opt_str = self.file_pattern.sub("^^\\1", " ".join(output_opt))
                if stdout_opt:
                    opt_str = "[" + opt_str + "]"
                str = opt_str + " " + str
            lines.append(str)
        return lines
