from typing import Any

from celery.backends.base import Backend

class RPCBackend(Backend):
    def __init__(
        self,
        url: str | None = None,
        result_exchange: str | None = None,
        result_exchange_type: str | None = None,
        **kwargs: Any,
    ) -> None: ...
