from collections.abc import Callable
from typing import Any

class Panel:
    data: dict[str, Callable[..., Any]]

    @classmethod
    def register(
        cls,
        method: Callable[..., Any],
        name: str | None = None,
    ) -> Callable[..., Any]: ...

def control_command(
    args: list[tuple[str, str]] | None = None,
    signature: str | None = None,
    variadic: str | None = None,
    **options: Any,
) -> Callable[[Callable[..., Any]], Callable[..., Any]]: ...
def inspect_command(
    args: list[tuple[str, str]] | None = None,
    signature: str | None = None,
    variadic: str | None = None,
    **options: Any,
) -> Callable[[Callable[..., Any]], Callable[..., Any]]: ...
