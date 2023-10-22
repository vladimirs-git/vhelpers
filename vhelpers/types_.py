"""Typing."""
from datetime import date
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

# 2 level
LParam = List[Param]
LT = List[T]
ST = Set[T]
TT = Tuple[T]
SParam = Set[Param]
SeqT = Sequence[T]
TParam = Tuple[Param, ...]

# 3 level
UParam = Union[LParam, SParam, TParam]
UT = Union[LT, ST, TT]
