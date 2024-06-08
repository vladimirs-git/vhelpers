"""Helper functions."""
from vhelpers.types_ import UStr, LStr


def init_cmds(config: UStr) -> LStr:
    """Convert config to list of commands."""
    if isinstance(config, str):
        cmds = config.splitlines()
    else:
        cmds = list(config)
    return cmds
