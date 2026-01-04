from collections.abc import Callable
from typing import Any

import kombu

from celery.app.base import Celery
from celery.bootsteps import Blueprint

class Consumer:
    app: Celery
    hostname: str
    pool: Any
    connection: kombu.Connection | None
    blueprint: Blueprint

    def __init__(
        self,
        on_task_request: Callable[..., Any],
        hostname: str | None = None,
        pool: Any = None,
        app: Celery | None = None,
        timer: Any = None,
        controller: Any = None,
        hub: Any = None,
        amqheartbeat: float | None = None,
        worker_options: dict[str, Any] | None = None,
        disable_rate_limits: bool = False,
        initial_prefetch_count: int = 2,
        prefetch_multiplier: int = 4,
        **kwargs: Any,
    ) -> None: ...
    def bucket_for_task(self, type: Any) -> Any: ...
    def reset_rate_limits(self) -> None: ...
    def add_task_queue(
        self,
        queue: str | kombu.Queue,
        exchange: str | kombu.Exchange | None = None,
        exchange_type: str | None = None,
        routing_key: str | None = None,
        **options: Any,
    ) -> kombu.Queue: ...
    def cancel_task_queue(self, queue: str | kombu.Queue) -> None: ...
    def apply_eta_task(self, task: Any) -> None: ...
    def call_soon(
        self,
        callback: Callable[..., Any],
        *args: Any,
        **kwargs: Any,
    ) -> None: ...
    def connect(self) -> kombu.Connection: ...
    def close_connection(self) -> None: ...
    def stop(self) -> None: ...
    def start(self) -> None: ...
    def restart(self) -> None: ...
    def shutdown(self) -> None: ...
    def reload_queues(self) -> None: ...
    def register_with_event_loop(self, hub: Any) -> None: ...
    def on_poll_init(self, hub: Any) -> None: ...
    @property
    def info(self) -> dict[str, Any]: ...
