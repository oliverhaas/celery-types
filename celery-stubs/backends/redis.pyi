from typing import Any

from celery.backends.base import KeyValueStoreBackend

class RedisBackend(KeyValueStoreBackend):
    def __init__(
        self,
        url: str | None = None,
        host: str | None = None,
        port: int | None = None,
        db: int | None = None,
        password: str | None = None,
        max_connections: int | None = None,
        **kwargs: Any,
    ) -> None: ...

class SentinelBackend(RedisBackend):
    def __init__(
        self,
        url: str | None = None,
        sentinels: list[tuple[str, int]] | None = None,
        sentinel_timeout: float | None = None,
        socket_timeout: float | None = None,
        **kwargs: Any,
    ) -> None: ...
