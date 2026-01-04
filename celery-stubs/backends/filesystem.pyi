from typing import Any

from celery.backends.base import KeyValueStoreBackend

class FilesystemBackend(KeyValueStoreBackend):
    def __init__(
        self,
        url: str | None = None,
        open: Any = ...,
        unlink: Any = ...,
        sep: str = ...,
        encoding: str = ...,
        **kwargs: Any,
    ) -> None: ...
