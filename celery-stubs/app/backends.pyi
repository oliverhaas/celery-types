from typing import Any

from celery.backends.base import Backend

BACKEND_ALIASES: dict[str, str]

def by_name(backend: str | None = None, loader: Any | None = None) -> type[Backend]: ...
def by_url(backend: str, loader: Any | None = None) -> type[Backend]: ...
