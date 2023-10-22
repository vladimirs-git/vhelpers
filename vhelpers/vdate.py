"""Helpers for date processing."""
import os
from datetime import datetime

from vhelpers.types_ import LStr, SDate


def last_modified_date(files: LStr) -> str:
    """Last modified dates."""
    dates: SDate = set()
    for path in files:
        stat = os.stat(path)
        date_ = datetime.fromtimestamp(stat.st_mtime).date()
        dates.add(date_)
    if not dates:
        return ""
    date_max = max(dates)
    return str(date_max)
