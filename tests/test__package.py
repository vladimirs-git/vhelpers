"""unittests package"""

import re
from pathlib import Path

from vhelpers import vdate, vdict, vpath, vre

ROOT = Path(__file__).parent.parent
PYPROJECT_D = vdict.pyproject_d(ROOT)


def test__version__readme():
    """Version in README, URL."""
    package = PYPROJECT_D["tool"]["poetry"]["name"].replace("_", "-")
    readme_file = PYPROJECT_D["tool"]["poetry"]["readme"]
    dwl_url = PYPROJECT_D["tool"]["poetry"]["urls"]["Download URL"]
    readme_text = Path.joinpath(ROOT, readme_file).read_text(encoding="utf-8")
    version_exp = PYPROJECT_D["tool"]["poetry"]["version"]

    for source, text in [
        (readme_file, readme_text),
        ("pyproject.toml project.urls.DownloadURL", dwl_url),
    ]:
        is_regex_found = False
        for regex in [
            package + r".+/(.+?)\.tar\.gz",
            package + r"@(.+?)$",
        ]:
            versions = re.findall(regex, text, re.M)
            for version in versions:
                is_regex_found = True
                assert version == version_exp
        assert is_regex_found is True, f"absent {version_exp} in {source}"


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
    files = vpath.get_files(ROOT, ext=".py")
    last_modified = vdate.last_modified(files)
    assert last_modified == date_log, f"Need update last modified date in {path}"
