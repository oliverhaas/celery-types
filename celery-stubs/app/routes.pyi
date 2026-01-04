from typing import Any

from celery.app.base import Celery

class Router:
    def __init__(
        self,
        routes: Any = ...,
        queues: Any = ...,
        create_missing: bool = ...,
        app: Celery | None = ...,
    ) -> None: ...
