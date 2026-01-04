from typing import Any

from celery.backends.base import Backend

class CassandraBackend(Backend):
    def __init__(
        self,
        servers: list[str] | None = None,
        keyspace: str | None = None,
        table: str | None = None,
        entry_ttl: int | None = None,
        port: int | None = None,
        **kwargs: Any,
    ) -> None: ...
