from typing import Any

from celery.app.base import Celery
from celery.security.serialization import SecureSerializer

def setup_security(
    allowed_serializers: list[str] | None = None,
    key: str | None = None,
    cert: str | None = None,
    store: str | None = None,
    digest: str = "sha256",
    serializer: str = "json",
    app: Celery | None = None,
    key_password: str | None = None,
) -> None: ...
def disable_untrusted_serializers(
    allowed: list[str] | None = None,
) -> None: ...
