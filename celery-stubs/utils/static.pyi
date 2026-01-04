from typing import Any, Generic, TypeVar

_T = TypeVar("_T")

class static(Generic[_T]):
    thing: _T
    def __init__(self, thing: _T) -> None: ...
    def __call__(self) -> _T: ...
