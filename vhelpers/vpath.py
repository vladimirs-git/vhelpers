"""Helpers for path processing."""
import os
from pathlib import Path

from vhelpers.types_ import LStr, UPath


def get_files(root: UPath, ext: str) -> LStr:
    """Get paths to files with required extension in root directory.

    :param str root: Root directory to search for files with required extension.
    :param ext: Extension, end of file name.
    :return: A list of paths with required extension.
    """
    paths: LStr = []
    for root_i, _, files_i in os.walk(str(root)):
        for file_ in files_i:
            if file_.endswith(ext):
                path = os.path.join(root_i, file_)
                paths.append(path)
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
