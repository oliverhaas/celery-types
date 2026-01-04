from collections.abc import Callable
from typing import Any

def add_autoretry_behaviour(
    task: Any,
    autoretry_for: tuple[type[BaseException], ...] | None = None,
    retry_kwargs: dict[str, Any] | None = None,
    retry_backoff: bool | int = False,
    retry_backoff_max: int = 600,
    retry_jitter: bool = True,
) -> Callable[..., Any]: ...
