from typing import Any

from celery.backends.base import Backend

class CouchBackend(Backend):
    def __init__(
        self,
        url: str | None = None,
        container: str | None = None,
        **kwargs: Any,
    ) -> None: ...
