from typing import Any

from celery.backends.base import KeyValueStoreBackend

class CacheBackend(KeyValueStoreBackend):
    def __init__(
        self,
        backend: str | None = None,
        expires: float | None = None,
        options: dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> None: ...
