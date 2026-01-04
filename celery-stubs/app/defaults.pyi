from typing import Any, NamedTuple

class Option(NamedTuple):
    default: Any
    type: type | None = None
    aliases: tuple[str, ...] = ()
    deprecate_by: str | None = None
    remove_by: str | None = None

DEFAULTS: dict[str, dict[str, Any]]
NAMESPACES: dict[str, dict[str, Option]]
SETTING_KEYS: frozenset[str]

def find(name: str, namespace: str = "celery") -> tuple[str, Option] | None: ...
def strtobool(term: str | bool | int | None) -> bool: ...
