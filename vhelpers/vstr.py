"""Helpers for string processing."""


def repr_params(*args, **kwargs) -> str:
    """Create parameters for the __repr__() method.

    :param args: The positional arguments.
    :param kwargs: The keyword arguments.
    :return: A string representation of the parameters.
    :example: repr_params("a", "b", c="c", d="d") -> "'a', 'b', c='c', d='d'"
    """
    args_ = ", ".join([f"{v!r}" for v in args if v])
    kwargs_ = ", ".join([f"{k}={v!r}" for k, v in kwargs.items() if v])
    params = [s for s in (args_, kwargs_) if s]
    return ", ".join(params)
