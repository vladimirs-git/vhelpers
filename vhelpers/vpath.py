"""Helpers for path processing."""
import os

from vhelpers.types_ import LStr, UPath


def get_files(root: UPath, ext: str) -> LStr:
    """Get paths to .py files if root directory tree.

    :param root: The root directory to search for .py files.
    :param ext: Extension, end of file name.
    :return: A list of paths to .py files.
    """
    paths: LStr = []
    for root_i, _, files_i in os.walk(str(root)):
        for file_ in files_i:
            if file_.endswith(ext):
                path = os.path.join(root_i, file_)
                paths.append(path)
    return paths
