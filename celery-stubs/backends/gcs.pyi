from typing import Any

from celery.backends.base import KeyValueStoreBackend

class GCSBackend(KeyValueStoreBackend):
    def __init__(
        self,
        url: str | None = None,
        bucket: str | None = None,
        base_path: str | None = None,
        project: str | None = None,
        **kwargs: Any,
    ) -> None: ...
