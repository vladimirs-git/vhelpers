"""Typing."""
from datetime import date
from pathlib import Path
from typing import Any, Dict, List, Sequence, Set, Tuple, TypeVar, Union

# 1 level
DAny = Dict[str, Any]
LStr = List[str]
Param = Tuple[str, Any]
SDate = Set[date]
T = TypeVar("T")
T2Str = Tuple[str, str]
T3Str = Tuple[str, str, str]
T4Str = Tuple[str, str, str, str]
TList = (list, set, tuple)
UPath = Union[Path, str]

# 2 level
LParam = List[Param]
LT = List[T]
SParam = Set[Param]
ST = Set[T]
SeqT = Sequence[T]
TParam = Tuple[Param, ...]
TT = Tuple[T]

# 3 level
UParam = Union[LParam, SParam, TParam]
UT = Union[LT, ST, TT]
