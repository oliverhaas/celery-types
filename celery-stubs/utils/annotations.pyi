from collections.abc import Mapping
from typing import Any

def resolve_all(
    app: Any,
    d: Mapping[str, Any],
    filter: Any | None = None,
) -> dict[str, Any]: ...
