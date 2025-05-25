"""Helpers for string processing."""

from vhelpers.types_ import LStr, T2Str


def join(*args) -> str:
    """Join args by delimiter that is first argument, skipping empty strings.

    :param args: Items that need to be joined.
    :return: Joined string.

    :example:
        join(",", "a", "", 0, 1) -> "a,0,1"
    """
    if not args:
        return ""

    delimiter = args[0]
    args = args[1:]

    items: LStr = []
    for item in args:
        if isinstance(item, str):
            if item:
                items.append(item)
        else:
            items.append(str(item))

    return delimiter.join(items)


def join_lines(*args) -> str:
    r"""Join args by new-line character, skipping empty strings.

    :param args: Items that need to be joined.
    :return: Joined string.

    :example:
        join_lines("a", "", 0, 1) -> "a\n0\n1"
    """
    return join("\n", *args)


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


def split_idx(text: str, idx: int) -> T2Str:
    """Split the text at the specified index.

    :param text: Text to split.
    :param idx: Index at which to split the text.
    :return: Tuple containing the text before the index and the text after the index.

    :example:
        split_idx(text="before_after", idx=7) -> "before_", "after"
    """
    before = text[:idx]
    after = text[idx:]
    return before, after
