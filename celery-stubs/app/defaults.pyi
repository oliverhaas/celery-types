from builtins import type as _type
from typing import Any

__all__: tuple[str, ...]

class Option:
    default: Any
    type: str | None
    deprecate_by: str | None
    remove_by: str | None
    alt: tuple[str, ...] | None
    old: set[str]
    typemap: dict[str, _type]

    def __init__(
        self,
        default: Any,
        type: str | _type | None = None,  # noqa: A002
        deprecate_by: str | None = None,
        remove_by: str | None = None,
        alt: tuple[str, ...] | None = None,
    ) -> None: ...
    def to_python(self, value: Any) -> Any: ...

DEFAULTS: dict[str, dict[str, Any]]
NAMESPACES: dict[str, dict[str, Option]]
SETTING_KEYS: frozenset[str]

def find(name: str, namespace: str = "celery") -> tuple[str, Option] | None: ...
def flatten(d: dict[str, dict[str, Any]], ns: str = "") -> dict[str, Any]: ...
def strtobool(term: str | bool | int | None) -> bool: ...
