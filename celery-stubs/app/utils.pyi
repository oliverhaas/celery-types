from typing import Any

from celery.utils.collections import ConfigurationView

class Settings(ConfigurationView):  # type: ignore[misc]  # pyright: ignore[reportImplicitAbstractClass]
    def __init__(
        self, *args: Any, deprecated_settings: set[str] | None = None, **kwargs: Any
    ) -> None: ...
