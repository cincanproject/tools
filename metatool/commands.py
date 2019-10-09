import pathlib
import re
import string

from typing import List, Set, Dict, Tuple, Optional, Any, Iterable


def quote_args(args: Iterable[str]) -> List[str]:
    """Quote the arguments which contain whitespaces (only for printing)"""
    r = []
    for arg in args:
        if any(map(lambda c: c in string.whitespace, arg)):
            r.append(f'"{arg}"')
        else:
            r.append(arg)
    return r


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
    def __init__(self, json: Dict[str,Any], command_args: List[str] = None):
        self.commands_json = json.get('commands', [])
        # NOTE: The same regexp as in dockertools.py :/
        self.file_pattern = re.compile("^([^\\^]*)\\^([^, :\"\']+)(.*)$")

        # create ad-hoc command if ^ given in tool arguments (forget the ones in commands.json)
        if command_args and len(command_args) > 0:
            self.commands_json = [{'command': command_args}]

    def is_output_to_file_option(self) -> bool:
        """Is there option to capture native tool output into a file or directory?"""
        for c in self.commands_json:
            m = [a for a in c.get('command', []) if self.file_pattern.match(a)]
            if any(map(lambda s: s.startswith('^^'), m)):
                return True
        return False

    def command_line(self, in_file: str, args: List[str] = None,
                     in_type: Optional[str] = None, out_type: Optional[str] = None,
                     write_output: Optional[str] = None) -> ToolCommand:
        """Create the native tool command line with input/output markers"""
        all_commands = self.commands_json
        match_commands = []
        match_in_type = None
        match_out_type = None
        for c in self.commands_json:
            if not any(map(lambda s: self.file_pattern.match(s), c['command'])):
                continue
            if in_type is not None and in_type not in c.get('input', [in_type]):
                continue
            if out_type is not None and out_type not in c.get('output', [out_type]):
                continue
            match_commands.append(c)
            match_in_type = c.get('input')
            match_out_type = c.get('output')
        if len(match_commands) != 1:
            raise Exception("Single command should match given input/output filter, now:\n{}".format(
                "\n".join(map(lambda x: "{}{}".format(" -I {}".format(x['input']) if 'input' in x else "",
                                                      " -O {}".format(x['output']) if 'output' in x else ""),
                              match_commands))))
        command = match_commands[0]['command']
        true_args = []
        for arg in (command + args if args else command):
            m = self.file_pattern.match(arg)
            n_arg = arg
            if m is not None:
                b_name = m.group(2)
                download = b_name.startswith('^')
                if not download:
                    n_arg = m.group(1) + "^" + in_file + m.group(3)
                elif write_output:
                    n_arg = m.group(1) + "^^" + write_output + m.group(3)
            true_args.append(n_arg)
        return ToolCommand(true_args, in_file=in_file, in_type=match_in_type,
                           out_file=write_output, out_type=match_out_type)

    def commands_from_metadata(self, metadata: Optional[Dict[str, Any]], root_dir: str, all_files: Iterable[str],
                               write_output: Optional[str] = None) -> List[ToolCommand]:
        """Create possible native tool command lines based on input metadata"""
        files = []
        if metadata:
            # metadata json lists which files to process, and perhaps types for them
            for f in metadata.get('files', []):
                f_name = f.get('name', 'stdout')
                dir_prefix = (root_dir + '/' if root_dir != '' else '') + f_name + '/'
                f_type = f.get('type')
                f_files = list(filter(lambda s: s == f_name or s.startswith(dir_prefix), all_files))
                files += map(lambda s: (s, f_type), f_files)
        else:
            # no metadata, just give root directory
            files.append((".", None))
        if not files:
            raise Exception("No matching files for processing")
        commands = []
        many_files = len(files) > 1
        for n, t in files:
            w_out = (pathlib.Path(write_output) / n).as_posix() if write_output and many_files else write_output
            cmd = self.command_line(in_file=n, in_type=t, write_output=w_out)
            commands.append(cmd)
        return commands

    def command_hints(self) -> List[str]:
        """List command hints, if any"""
        lines = []
        for c in self.commands_json:
            cmds = c['command']
            str = " ".join(cmds)
            lines.append(str)
        return lines
