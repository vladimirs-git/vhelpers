"""Typing."""
from datetime import date, datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Set, Tuple, TypeVar, Union

# 1 level
DAny = Dict[str, Any]
DInt = Dict[str, int]
Dtime = datetime
IntStr = Union[int, str]
LAny = List[Any]
LStr = List[str]
ODtime = Optional[datetime]
Param = Tuple[str, Any]
SDate = Set[date]
SStr = Set[str]
SeqStr = Sequence[str]
T = TypeVar("T")
T2Int = Tuple[int, int]
T2Str = Tuple[str, str]
T3Str = Tuple[str, str, str]
T4Str = Tuple[str, str, str, str]
TList = (list, set, tuple)
UPath = Union[Path, str]

# 2 level
DLStr = Dict[str, LStr]
LLAny = List[LAny]
LParam = List[Param]
LT = List[T]
LT3Str = List[T3Str]
SParam = Set[Param]
ST = Set[T]
SeqT = Sequence[T]
TParam = Tuple[Param, ...]
TT = Tuple[T]
UStr = Union[str, SeqStr]

# 3 level
UParam = Union[LParam, SParam, TParam]
UT = Union[LT, ST, TT]
T3Strs = Tuple[str, str, UStr]

# 4 level
LT3Strs = List[T3Strs]
