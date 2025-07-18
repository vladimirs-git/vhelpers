"""Helpers for path processing."""

import re
from pathlib import Path

from vhelpers.types_ import LStr, UPath


def get_dirs(root: UPath, pattern: str) -> LStr:
    """Get paths to directories that match required regex pattern in root directory.

    :param root: Root directory to search for directories with required pattern.
    :param pattern: Regex pattern to match directory path.
    :return: Paths to directories that match regex pattern.

    :example:
        get_dirs(root="/var/log/", pattern="dir") -> ["/var/log/dir"]
    """
    paths: LStr = []

    root_path = Path(root)
    for path in root_path.rglob("*"):
        if path.is_dir() and re.search(pattern, path.name):
            paths.append(path.as_posix())

    return paths


def get_files(root: UPath, pattern: str) -> LStr:
    """Get paths to files that match required regex pattern in root directory.

    :param root: Root directory to search for files with required pattern.
    :param pattern: Regex pattern to match file path.
    :return: Paths to files that match regex pattern.

    :example:
        get_files(root="/var/log/", pattern="log$") -> ["/var/log/dir/file.log"]
    """
    paths: LStr = []

    root_path = Path(root)
    for path in root_path.rglob("*"):
        if path.is_file() and re.search(pattern, path.name):
            paths.append(path.as_posix())

    return paths


def to_dir(path: UPath, name: str) -> Path:
    """Get path to directory with required name.

    :param Path path: Path where need to find directory with required name.
    :param str name: Required directory name.
    :return: Path to directory with required name.
    """
    path_o = Path(path)
    while path_o.name != name:
        if not path_o.name:
            raise ValueError(f"{name=} has not been found in {path!s}")
        path_o = path_o.parent
    return path_o
