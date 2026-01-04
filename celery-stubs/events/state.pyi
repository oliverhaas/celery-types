from collections.abc import Callable, Iterator
from datetime import datetime
from typing import Any

class Task:
    # Attributes based on runtime inspection
    id: str | None
    uuid: str
    name: str | None
    state: str
    received: float | None
    sent: float | None
    started: float | None
    succeeded: float | None
    failed: float | None
    retried: float | None
    revoked: float | None
    rejected: float | None
    args: str | None
    kwargs: str | None
    eta: datetime | None
    expires: datetime | None
    retries: int | None
    result: Any
    exception: str | None
    traceback: str | None
    worker: Worker | None
    client: str | None
    clock: int | None
    timestamp: float | None
    origin: str | None
    root: str | None
    root_id: str | None
    parent: str | None
    parent_id: str | None
    exchange: str | None
    routing_key: str | None
    runtime: float | None

    merge_rules: dict[str, Any]

    def __init__(
        self,
        uuid: str | None = None,
        cluster_state: State | None = None,
        children: list[str] | None = None,
        **kwargs: Any,
    ) -> None: ...
    def event(
        self, type_: str | None, timestamp: float | None = None, **fields: Any
    ) -> str | None: ...
    def info(
        self,
        fields: list[str] | None = None,
        extra: list[str] | None = None,
    ) -> dict[str, Any]: ...
    def as_dict(self) -> dict[str, Any]: ...
    def ready(self) -> bool: ...

class Worker:
    hostname: str
    id: str | None
    pid: int | None
    freq: float
    heartbeats: list[float]
    clock: int
    active: int | None
    processed: int | None
    loadavg: list[float] | None
    sw_ident: str | None
    sw_ver: str | None
    sw_sys: str | None
    expire_window: float
    heartbeat_max: int

    def __init__(
        self,
        hostname: str | None = None,
        pid: int | None = None,
        freq: float = 60,
        heartbeats: list[float] | None = None,
        clock: int = 0,
        active: int | None = None,
        processed: int | None = None,
        loadavg: list[float] | None = None,
        sw_ident: str | None = None,
        sw_ver: str | None = None,
        sw_sys: str | None = None,
        **kwargs: Any,
    ) -> None: ...
    def update(
        self,
        **fields: Any,
    ) -> None: ...
    def event(
        self, type_: str | None, timestamp: float | None = None, **fields: Any
    ) -> str | None: ...
    @property
    def heartbeat_expires(self) -> float: ...
    @property
    def alive(self) -> bool: ...
    @property
    def status_string(self) -> str: ...

_Task = Task
_Worker = Worker

class State:
    event_count: int
    task_count: int
    heap_multiplier: int
    max_workers_in_memory: int
    max_tasks_in_memory: int

    Task: type[_Task]
    Worker: type[_Worker]

    def __init__(
        self,
        callback: Callable[..., Any] | None = None,
        workers: dict[str, _Worker] | None = None,
        tasks: dict[str, _Task] | None = None,
        taskheap: Any = None,
        max_workers_in_memory: int = 5000,
        max_tasks_in_memory: int = 10000,
        on_node_join: Callable[..., Any] | None = None,
        on_node_leave: Callable[..., Any] | None = None,
    ) -> None: ...
    def freeze_while(self, f: Callable[..., Any], *args: Any, **kwargs: Any) -> Any: ...
    def clear_tasks(self, ready: bool = True) -> None: ...
    def clear(self, ready: bool = True) -> None: ...
    def get_or_create_worker(self, hostname: str, **kwargs: Any) -> tuple[_Worker, bool]: ...
    def get_or_create_task(self, uuid: str) -> tuple[_Task, bool]: ...
    def worker_event(self, type_: str, fields: dict[str, Any]) -> tuple[_Worker, bool] | tuple[None, bool]: ...
    def task_event(self, type_: str, fields: dict[str, Any]) -> tuple[_Task, bool] | tuple[None, bool]: ...
    def event(self, event: dict[str, Any]) -> tuple[_Worker | _Task | None, bool]: ...
    def rebuild_taskheap(self, timetuple: Callable[..., Any] = ...) -> None: ...
    def itertasks(self, limit: int | None = None) -> Iterator[tuple[str, _Task]]: ...
    def tasks_by_time(self, limit: int | None = None, reverse: bool = True) -> list[tuple[str, _Task]]: ...
    def tasks_by_timestamp(self, limit: int | None = None, reverse: bool = True) -> list[tuple[str, _Task]]: ...
    def task_types(self) -> set[str]: ...
    def alive_workers(self) -> list[_Worker]: ...
