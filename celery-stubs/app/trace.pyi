from collections.abc import Callable
from logging import Logger
from typing import Any, NamedTuple

from celery.app.base import Celery
from celery.app.task import Task

class TraceInfo(NamedTuple):
    state: str
    retval: Any

def build_tracer(
    name: str,
    task: Task[..., Any],
    loader: Any | None = None,
    hostname: str | None = None,
    store_errors: bool = True,
    Info: type = TraceInfo,
    eager: bool = False,
    propagate: bool = False,
    app: Celery | None = None,
    monotonic: Callable[[], float] = ...,
    trace_ok_t: type = ...,
    IGNORE_STATES: frozenset[str] = ...,
) -> Callable[..., Any]: ...
def trace_task(
    task: Task[..., Any],
    uuid: str,
    args: tuple[Any, ...],
    kwargs: dict[str, Any],
    request: Any | None = None,
    **opts: Any,
) -> TraceInfo: ...
def trace_task_ret(
    name: str,
    uuid: str,
    request: Any,
    body: Any,
    content_type: str,
    content_encoding: str,
    loads: Callable[..., Any] = ...,
    _: Any = None,
    **extra_request: Any,
) -> TraceInfo: ...
def fast_trace_task(
    task: Task[..., Any],
    uuid: str,
    request: Any,
    body: Any,
    content_type: str,
    content_encoding: str,
    loads: Callable[..., Any] = ...,
    _: Any = None,
    __: Any = None,
    hostname: str | None = None,
    **extra_request: Any,
) -> TraceInfo: ...
def setup_worker_optimizations(app: Celery, hostname: str | None = None) -> None: ...
def reset_worker_optimizations() -> None: ...

logger: Logger
