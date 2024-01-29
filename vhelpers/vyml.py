"""Helpers for YAML processing."""

from vhelpers.types_ import LStr, UStr, LT3Strs, DLStr


def host_cmds(items: LT3Strs) -> str:
    """Create commands in YAML format.

    Where the hostname is the key and the list of commands is the value.
    :param items: List of tuples that contain: hostname, parent command, children commands.
    :return: YAML formatted commands.

    :example:
        items = [("router1", "interface Ethernet1/1", ["description text", "shutdown"])]
        host_cmds(items) -> "
    ---
    host1: |
     cmdA
       cmd1
       cmd2
    "
    """
    hostnames = sorted([t[0] for t in items])
    configs_d: DLStr = {s: [] for s in hostnames}
    for hostname, cmd, cmds in items:
        config = cmd_cmds(cmd=cmd, cmds=cmds)
        configs_d[hostname].append(config)

    yaml_l: LStr = ["---"]
    for hostname, configs in configs_d.items():
        config = "\n".join(configs)
        yaml_l.extend([f"{hostname}: |", config])
    return "\n".join(yaml_l)


def cmd_cmds(cmd: str = "", cmds: UStr = "") -> str:
    """Join parent command and children commands using indentation.

    :param cmd: Parent command.
    :param cmds: Children commands.
    :return: YAML formatted commands with indentation.

    :example:
        cmd_cmds(cmd="cmdA", cmds=["cmd1", "cmd2"]) -> "
     cmdA
       cmd1
       cmd2
    "
    """
    if not cmds:
        return ""
    if isinstance(cmds, str):
        cmds = cmds.split("\n")
    cmds_: LStr = [s.strip() for s in list(cmds)]
    if cmds_ and cmds_[0] == "":
        cmds_ = cmds_[1:]
    if cmds_ and cmds_[-1] == "":
        cmds_ = cmds_[:-1]
    cmds_ = [f"  {s}" for s in cmds_]
    if cmd:
        cmds_.insert(0, f" {cmd.strip()}")
    return "\n".join(cmds_)
