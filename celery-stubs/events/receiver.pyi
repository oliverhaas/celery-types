from collections.abc import Callable, Iterable, Iterator
from contextlib import contextmanager
from typing import Any

import kombu

from celery.app.base import Celery

class EventReceiver:
    Consumer: type[Any]
    app: Celery
    connection: kombu.Connection
    handlers: dict[str, Callable[..., Any]]
    channel_errors: tuple[type[Exception], ...]
    connection_errors: tuple[type[Exception], ...]
    connect_max_retries: int | None
    restart_limit: Any
    should_stop: bool

    def __init__(
        self,
        channel: Any,
        handlers: dict[str, Callable[..., Any]] | None = None,
        routing_key: str = "#",
        node_id: str | None = None,
        app: Celery | None = None,
        queue_prefix: str = "celeryev",
        accept: Iterable[str] | None = None,
        queue_ttl: float | None = None,
        queue_expires: float | None = None,
    ) -> None: ...
    def process(
        self,
        type: str,
        event: dict[str, Any],
    ) -> None: ...
    def capture(
        self,
        limit: int | None = None,
        timeout: float | None = None,
        wakeup: bool = True,
    ) -> None: ...
    def itercapture(
        self,
        limit: int | None = None,
        timeout: float | None = None,
        wakeup: bool = True,
    ) -> Iterator[tuple[str, dict[str, Any]]]: ...
    def consume(
        self,
        limit: int | None = None,
        timeout: float | None = None,
        wakeup: bool = True,
    ) -> None: ...
    def run(
        self,
        limit: int | None = None,
        timeout: float | None = None,
        wakeup: bool = True,
    ) -> None: ...
    @contextmanager
    def consumer_context(self, wakeup: bool = True) -> Iterator[kombu.Consumer]: ...
    def on_consume_ready(
        self,
        connection: Any,
        channel: Any,
        consumers: list[Any],
        wakeup: bool = True,
        **kwargs: Any,
    ) -> None: ...
    def on_consume_end(self, connection: Any, channel: Any) -> None: ...
    def on_connection_revived(self) -> None: ...
    def on_connection_error(self, exc: Exception, interval: float) -> None: ...
    def on_decode_error(self, message: Any, exc: Exception) -> None: ...
    def on_iteration(self) -> None: ...
    def maybe_conn_error(self, fun: Callable[..., Any]) -> Any: ...
    def create_connection(self) -> kombu.Connection: ...
    def establish_connection(self) -> kombu.Connection: ...
    @contextmanager
    def extra_context(
        self, connection: kombu.Connection, channel: Any
    ) -> Iterator[None]: ...
    def event_from_message(
        self, body: Any, message: Any
    ) -> tuple[str, dict[str, Any]]: ...
    def get_consumers(self, consumer: type[Any], channel: Any) -> list[Any]: ...
    def wakeup_workers(self, channel: Any) -> None: ...
