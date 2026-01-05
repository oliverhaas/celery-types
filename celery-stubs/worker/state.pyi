from collections.abc import Callable, MutableSet
from typing import Any

class Persistent:
    db: Any
    merge: Callable[..., Any]
    open: Callable[..., Any]

    def __init__(self, state: Any, filename: str, clock: Any | None = None) -> None: ...
    def save(self) -> None: ...

C_BENCH: bool
C_BENCH_EVERY: int
REVOKES_MAX: int
REVOKE_EXPIRES: int
SUCCESSFUL_EXPIRES: int
SUCCESSFUL_MAX: int
SOFTWARE_INFO: dict[str, str]

revoked: MutableSet[str]
revoked_stamps: dict[str, set[str]]
active_requests: MutableSet[Any]
reserved_requests: MutableSet[Any]
successful_requests: MutableSet[Any]
requests: dict[str, Any]
total_count: dict[str, int]
all_total_count: list[int]

should_stop: bool
should_terminate: bool

def maybe_shutdown() -> None: ...
def reset_state() -> None: ...
def task_accepted(request: Any, _all_total_count: list[int] = ...) -> None: ...
def task_reserved(request: Any) -> None: ...
def task_ready(request: Any) -> None: ...
