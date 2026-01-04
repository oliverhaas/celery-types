from typing import Any

from celery.backends.base import KeyValueStoreBackend

class ArangoDbBackend(KeyValueStoreBackend):
    def __init__(
        self,
        url: str | None = None,
        host: str | None = None,
        port: int | None = None,
        database: str | None = None,
        collection: str | None = None,
        username: str | None = None,
        password: str | None = None,
        http_protocol: str | None = None,
        **kwargs: Any,
    ) -> None: ...
