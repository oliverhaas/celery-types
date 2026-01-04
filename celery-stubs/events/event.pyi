from collections.abc import Callable
from typing import Any

def Event(
    type: str,
    _fields: dict[str, Any] | None = None,
    __dict__: dict[str, Any] = ...,
    __now__: Callable[[], float] | None = None,
    **fields: Any,
) -> dict[str, Any]: ...
def group_from(type: str) -> str: ...
def get_exchange(conn: Any, name: str = ...) -> Any: ...
