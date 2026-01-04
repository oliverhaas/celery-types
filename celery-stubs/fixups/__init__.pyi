from typing import Any

from celery.app.base import Celery

def fixup(app: Celery, env: str | None = None) -> Any: ...
