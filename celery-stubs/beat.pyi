import shelve
from collections.abc import Callable
from datetime import datetime
from threading import Thread
from typing import Any, NamedTuple

import kombu
from celery.app.base import Celery
from celery.schedules import BaseSchedule
from typing_extensions import override

__all__ = [
    "PersistentScheduler",
    "ScheduleEntry",
    "Scheduler",
    "SchedulingError",
    "Service",
]

class SchedulingError(Exception): ...

class BeatLazyFunc:
    def __init__(self, func: Callable[..., Any], *args: Any, **kwargs: Any) -> None: ...

class ScheduleEntry:
    total_run_count: int
    name: str | None
    task: str | None
    last_run_at: datetime | None
    schedule: BaseSchedule | None
    args: tuple[Any, ...] | None
    kwargs: dict[str, Any] | None
    options: dict[str, Any] | None
    relative: bool
    app: Celery | None

    def __init__(
        self,
        name: str | None = None,
        task: str | None = None,
        last_run_at: datetime | None = None,
        total_run_count: int | None = None,
        schedule: BaseSchedule | None = None,
        args: tuple[Any, ...] = (),
        kwargs: dict[str, Any] | None = None,
        options: dict[str, Any] | None = None,
        relative: bool = False,
        app: Celery | None = None,
    ) -> None: ...

class event_t(NamedTuple):
    time: float
    priority: int
    entry: ScheduleEntry

class Scheduler:
    Entry: type[ScheduleEntry]
    app: Celery
    schedule: dict[str, ScheduleEntry]
    max_interval: int | None
    lazy: bool

    def __init__(
        self,
        app: Celery,
        schedule: dict[str, ScheduleEntry] | None = None,
        max_interval: int | None = None,
        Producer: type[kombu.Producer] | None = None,
        lazy: bool = False,
        sync_every_tasks: int | None = None,
        **kwargs: Any,
    ) -> None: ...
    def setup_schedule(self) -> None: ...
    def sync(self) -> None: ...
    def close(self) -> None: ...

class PersistentScheduler(Scheduler):
    persistence: type[shelve.Shelf[Any]]
    @override
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @override
    def setup_schedule(self) -> None: ...
    @override
    def sync(self) -> None: ...
    @override
    def close(self) -> None: ...

class Service:
    scheduler_cls: type[PersistentScheduler]
    app: Celery
    max_interval: int | None

    def __init__(
        self,
        app: Celery,
        max_interval: int | None = None,
        schedule_filename: str | None = None,
        scheduler_cls: type[Scheduler] | None = None,
    ) -> None: ...
    def start(self, embedded_process: bool = ...) -> None: ...
    def sync(self) -> None: ...
    def stop(self, wait: bool = ...) -> None: ...
    def get_scheduler(
        self, lazy: bool = ..., extension_namespace: str = ...
    ) -> Scheduler: ...
    @property
    def scheduler(self) -> Scheduler: ...

class _Threaded(Thread):
    daemon: bool
    name: str
    app: Celery

    def __init__(self, app: Celery, **kwargs: Any) -> None: ...
    @override
    def run(self) -> None: ...
    def stop(self) -> None: ...

class _Process:
    name: str
    app: Celery

    def __init__(self, app: Celery, **kwargs: Any) -> None: ...
    def run(self) -> None: ...
    def stop(self) -> None: ...
