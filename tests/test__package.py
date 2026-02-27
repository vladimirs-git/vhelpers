"""unittests package"""

import re
from pathlib import Path

from vhelpers import vdate, vdict, vpath, vre
from vhelpers.types_ import LStr

ROOT = Path(__file__).parent.parent
PYPROJECT_D = vdict.pyproject_d(ROOT)


def test__version__changelog():
    """Version in CHANGELOG."""
    version_toml = PYPROJECT_D["tool"]["poetry"]["version"]
    path = Path.joinpath(ROOT, "CHANGELOG.rst")
    text = path.read_text(encoding="utf-8")
    regex = r"(.+)\s\(\d\d\d\d-\d\d-\d\d\)$"
    version_log = vre.find1(regex, text, re.M)
    assert version_toml == version_log, f"Need update version in {path=}"


def test__last_modified_date():
    """Last modified date in CHANGELOG."""
    path = Path.joinpath(ROOT, "CHANGELOG.rst")
    text = path.read_text(encoding="utf-8")
    regex = r".+\((\d\d\d\d-\d\d-\d\d)\)$"
    date_log = vre.find1(regex, text, re.M)
    re_extension = "|".join(["py", "toml"])
    files: LStr = vpath.get_files(ROOT, pattern=f"\.({re_extension})$")
    last_modified = vdate.last_modified(files)
    assert last_modified == date_log, f"Need update last modified date in {path}"
