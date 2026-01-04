from typing import Any

from celery.backends.base import KeyValueStoreBackend

class CouchbaseBackend(KeyValueStoreBackend):
    def __init__(
        self,
        url: str | None = None,
        bucket: str | None = None,
        **kwargs: Any,
    ) -> None: ...
