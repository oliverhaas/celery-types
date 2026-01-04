from typing import Any

from celery.backends.base import Backend

class DatabaseBackend(Backend):
    def __init__(
        self,
        dburi: str | None = None,
        engine_options: dict[str, Any] | None = None,
        url: str | None = None,
        **kwargs: Any,
    ) -> None: ...
