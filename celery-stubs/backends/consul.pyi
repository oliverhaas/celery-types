from typing import Any

from celery.backends.base import KeyValueStoreBackend

class ConsulBackend(KeyValueStoreBackend):
    def __init__(
        self,
        url: str | None = None,
        one_client: bool | None = None,
        **kwargs: Any,
    ) -> None: ...
