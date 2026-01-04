from typing import Any

from celery.backends.base import Backend

class MongoBackend(Backend):
    def __init__(
        self,
        url: str | None = None,
        database: str | None = None,
        taskmeta_collection: str | None = None,
        groupmeta_collection: str | None = None,
        **kwargs: Any,
    ) -> None: ...
