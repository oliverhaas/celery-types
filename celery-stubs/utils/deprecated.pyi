from collections.abc import Callable as _Callable
from typing import Any, TypeVar

_F = TypeVar("_F", bound=_Callable[..., Any])

DEPRECATION_FMT: str
PENDING_DEPRECATION_FMT: str

class CDeprecationWarning(UserWarning): ...
class CPendingDeprecationWarning(PendingDeprecationWarning): ...

def warn(
    description: str = "",
    deprecation: str | None = None,
    removal: str | None = None,
    alternative: str | None = None,
    stacklevel: int = 2,
) -> None: ...

class Callable:
    def __init__(
        self,
        fun: _Callable[..., Any],
        deprecation: str | None = None,
        removal: str | None = None,
        alternative: str | None = None,
    ) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...

class Property:
    def __init__(
        self,
        fget: _Callable[..., Any] | None = None,
        fset: _Callable[..., None] | None = None,
        fdel: _Callable[..., None] | None = None,
        doc: str | None = None,
        deprecation: str | None = None,
        removal: str | None = None,
        alternative: str | None = None,
    ) -> None: ...
    def __get__(self, obj: Any, type: type | None = None) -> Any: ...
    def __set__(self, obj: Any, value: Any) -> None: ...
    def __delete__(self, obj: Any) -> None: ...
