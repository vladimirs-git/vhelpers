"""Helpers for date processing."""
import datetime
import os

from vhelpers.types_ import LStr, SDate, DInt, Dtime, ODtime

TIME_FMT = "%Y-%m-%d %H:%M:%S"


def aged(delta_: DInt) -> str:
    """Convert time delta to elapsed time in the format %H:%M:%S.

    :param delta_: A dictionary containing the time difference in hours, minutes, and seconds.
    :return: A string representing the elapsed time in the format %H:%M:%S.
    :example:
        aged(hours=8810, minutes=3, seconds=4) -> "8810:03:04"
    """
    hours = delta_["hours"]
    minutes = delta_["minutes"]
    seconds = delta_["seconds"]
    return f"{hours:02}:{minutes:02}:{seconds:02}"


def delta(start: Dtime, end: ODtime = None) -> DInt:
    """Calculate the elapsed days, hours, minutes and seconds between two datetime objects.

    :param start: The starting datetime object.
    :param end: The ending datetime object. If None, the current datetime is used.
    :return: A dictionary containing the elapsed hours, minutes, and seconds.
        If end is None, update data in object.
    :example:
        delta(start="2001-01-02 2:3:4") -> dict(hours=8810, minutes=3, seconds=4)
    """
    if end is None:
        end = datetime.datetime.now()
    delta_ = end - start
    hours, _ = [int(round(t)) for t in divmod(delta_.total_seconds(), 3600)]
    minutes_all, seconds = [int(round(t)) for t in divmod(delta_.total_seconds(), 60)]
    minutes = minutes_all - hours * 60
    return {"hours": hours, "minutes": minutes, "seconds": seconds}


def delta_s(*args, **kwargs) -> str:
    """Calculate the elapsed time in the format %H:%M:%S.

    :param args: The arguments for calculating the time delta.
    :param kwargs: The keyword arguments for calculating the time delta.
    :return: The elapsed time in the format %H:%M:%S.
    """
    time_delta: DInt = delta(*args, **kwargs)
    time_aged = aged(time_delta)
    return time_aged


def last_modified(files: LStr) -> str:
    """Last modified dates."""
    dates: SDate = set()
    for path in files:
        stat = os.stat(path)
        date_ = datetime.datetime.fromtimestamp(stat.st_mtime).date()
        dates.add(date_)
    if not dates:
        return ""
    date_max = max(dates)
    return str(date_max)
