from typing import Any

from celery.backends.base import KeyValueStoreBackend

class ElasticsearchBackend(KeyValueStoreBackend):
    def __init__(
        self,
        url: str | None = None,
        index: str | None = None,
        doc_type: str | None = None,
        **kwargs: Any,
    ) -> None: ...
