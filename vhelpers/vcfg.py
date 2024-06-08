"""Helpers for config commands processing."""

from vhelpers.types_ import LStr, UStr


def cmd_key(key: str, config: UStr) -> str:
    """Find key in list of commands.

    :param key: Key of required command.
    :param config: Config commands where need to find value.
    :return: Key if it is found, empty string otherwise.

    :example:
        cmd_key("shutdown", ["shutdown"]) -> "shutdown"
    """
    cmds = _init_cmds(config)
    for cmd in cmds:
        if key == cmd:
            return key
    return ""


def cmd_value(key: str, config: UStr) -> str:
    """Find value in list of commands by required key.

    :param key: Key of required command.
    :param config: Config commands where need to find value.
    :return: Value if key is found, empty string otherwise.

    :example:
        cmd_value("description", ["description VALUE"]) -> "VALUE"
    """
    value = ""
    cmds = _init_cmds(config)
    for cmd in cmds:
        if cmd.startswith(key):
            value = cmd.replace(key, "", 1)
            break
    return value


def _init_cmds(config: UStr) -> LStr:
    """Convert config to list of commands."""
    if isinstance(config, str):
        cmds = config.splitlines()
    else:
        cmds = list(config)
    return cmds
