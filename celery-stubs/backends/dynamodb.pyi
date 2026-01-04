from typing import Any

from celery.backends.base import KeyValueStoreBackend

class DynamoDBBackend(KeyValueStoreBackend):
    def __init__(
        self,
        url: str | None = None,
        table_name: str | None = None,
        read_capacity_units: int | None = None,
        write_capacity_units: int | None = None,
        **kwargs: Any,
    ) -> None: ...
