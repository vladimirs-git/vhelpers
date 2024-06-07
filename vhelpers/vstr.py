"""Helpers for string processing."""


def cmd_value(key: str, cmd: str) -> str:
    """Find value in command by required key.

    :param key: Key of required command.
    :param cmd: Command where need to find value.
    :return: Value if key is found, empty string otherwise.

    :example:
        cmd_value("description", "description VALUE") -> "VALUE"
    """
    value = ""
    if cmd.startswith(key):
        value = cmd.replace(key, "", 1)
    return value


def repr_info(*args, **kwargs) -> str:
    """Create info without qutes for the __repr__() method.

    :param args: The positional arguments.
    :param kwargs: The keyword arguments.
    :return: A string representation of the parameters.

    :example:
        repr_info("a", "b", c="c", d="d") -> "a, b, c=c, d=d"
    """
    args_ = ", ".join([f"{v!s}" for v in args if v])
    kwargs_ = ", ".join([f"{k}={v!s}" for k, v in kwargs.items() if v])
    params = [s for s in (args_, kwargs_) if s]
    return ", ".join(params)


def repr_params(*args, **kwargs) -> str:
    """Create parameters in quotes for the __repr__() method.

    :param args: The positional arguments.
    :param kwargs: The keyword arguments.
    :return: A string representation of the parameters.

    :example:
        repr_params("a", "b", c="c", d="d") -> "'a', 'b', c='c', d='d'"
    """
    args_ = ", ".join([f"{v!r}" for v in args if v])
    kwargs_ = ", ".join([f"{k}={v!r}" for k, v in kwargs.items() if v])
    params = [s for s in (args_, kwargs_) if s]
    return ", ".join(params)


def reverse(line: str) -> str:
    """Reverse the characters in a string.

    :param line: The input string.
    :return: The reversed string.

    :example:
        reverse("abc") -> "cba"
    """
    return line[::-1]
