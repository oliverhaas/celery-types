from collections.abc import Callable
from threading import Thread
from typing import Any

class Schedule:
    queue: list[Entry]
    def __init__(self, max_interval: float | None = None, on_error: Callable[[Exception], None] | None = None) -> None: ...
    def enter_at(self, entry: Entry, eta: float | None = None, priority: int = 0) -> Entry: ...
    def enter_after(self, secs: float, entry: Entry, priority: int = 0) -> Entry: ...
    def cancel(self, tref: Any) -> None: ...
    def clear(self) -> None: ...
    def empty(self) -> bool: ...
    @property
    def next(self) -> Entry | None: ...

class Entry:
    fun: Callable[..., Any]
    args: tuple[Any, ...]
    kwargs: dict[str, Any]
    tref: Any

    def __init__(
        self,
        fun: Callable[..., Any],
        args: tuple[Any, ...] = (),
        kwargs: dict[str, Any] | None = None,
    ) -> None: ...
    def __call__(self) -> Any: ...
    def cancel(self) -> None: ...
    def cancelled(self) -> bool: ...

_Entry = Entry
_Schedule = Schedule

class Timer(Thread):
    Entry: type[_Entry]
    Schedule: type[_Schedule]
    running: bool
    on_tick: Callable[[float], None] | None

    def __init__(
        self,
        schedule: Any | None = None,
        on_tick: Callable[[float], None] | None = None,
        on_error: Callable[[Exception], None] | None = None,
        max_interval: float | None = None,
        **kwargs: Any,
    ) -> None: ...
    def call_after(
        self,
        secs: float,
        fun: Callable[..., Any],
        args: tuple[Any, ...] = (),
        kwargs: dict[str, Any] | None = None,
        priority: int = 0,
    ) -> _Entry: ...
    def call_at(
        self,
        eta: float,
        fun: Callable[..., Any],
        args: tuple[Any, ...] = (),
        kwargs: dict[str, Any] | None = None,
        priority: int = 0,
    ) -> _Entry: ...
    def call_repeatedly(
        self,
        secs: float,
        fun: Callable[..., Any],
        args: tuple[Any, ...] = (),
        kwargs: dict[str, Any] | None = None,
        priority: int = 0,
    ) -> _Entry: ...
    def enter(
        self,
        entry: _Entry,
        eta: float | None = None,
        priority: int = 0,
    ) -> _Entry: ...
    def enter_after(
        self,
        secs: float,
        entry: _Entry,
        priority: int = 0,
    ) -> _Entry: ...
    def exit_after(
        self,
        secs: float,
        priority: int = 10,
    ) -> None: ...
    def cancel(self, tref: Any) -> None: ...
    def clear(self) -> None: ...
    def empty(self) -> bool: ...
    def next(self) -> _Entry | None: ...
    def run(self) -> None: ...
    def stop(self) -> None: ...
    def ensure_started(self) -> None: ...
    @property
    def queue(self) -> list[Any]: ...
