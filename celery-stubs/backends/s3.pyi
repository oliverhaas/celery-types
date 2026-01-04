from typing import Any

from celery.backends.base import KeyValueStoreBackend

class S3Backend(KeyValueStoreBackend):
    def __init__(
        self,
        url: str | None = None,
        bucket_name: str | None = None,
        base_path: str | None = None,
        endpoint_url: str | None = None,
        aws_access_key_id: str | None = None,
        aws_secret_access_key: str | None = None,
        aws_region: str | None = None,
        **kwargs: Any,
    ) -> None: ...
