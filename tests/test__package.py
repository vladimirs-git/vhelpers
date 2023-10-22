"""unittests package"""

import re
from pathlib import Path

import tomli

import vhelpers


def _make_pyproject_d(root: Path) -> dict:
    """Return data of pyproject.toml."""
    path = Path.joinpath(root, "pyproject.toml")
    fh = path.open(mode="rb")
    pyproject_d = tomli.load(fh)
    return pyproject_d


ROOT = Path(__file__).parent.parent.resolve()
PYPROJECT = _make_pyproject_d(ROOT)


def test_version__readme():
    """Version in README, URL."""
    package = PYPROJECT["tool"]["poetry"]["name"].replace("_", "-")
    readme_file = PYPROJECT["tool"]["poetry"]["readme"]
    dwl_url = PYPROJECT["tool"]["poetry"]["urls"]["Download URL"]
    readme_text = Path.joinpath(ROOT, readme_file).read_text()
    version_exp = PYPROJECT["tool"]["poetry"]["version"]

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


def test_version__changelog():
    """Version in CHANGELOG."""
    version_toml = PYPROJECT["tool"]["poetry"]["version"]
    path = Path.joinpath(ROOT, "CHANGELOG.rst")
    text = path.read_text()
    regex = r"(.+)\s\(\d\d\d\d-\d\d-\d\d\)$"
    version_log = vhelpers.findall1(regex, text, re.M)
    assert version_toml == version_log, f"version in {path=}"


def test_last_modified_date():
    """Last modified date in CHANGELOG."""
    path = Path.joinpath(ROOT, "CHANGELOG.rst")
    text = path.read_text()
    regex = r".+\((\d\d\d\d-\d\d-\d\d)\)$"
    date_log = vhelpers.findall1(regex, text, re.M)
    files = vhelpers.get_files(root=str(ROOT), ext=".py")
    last_modified = vhelpers.last_modified_date(files)
    assert last_modified == date_log, f"last modified file"
