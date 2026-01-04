from typing import Any

QUORUM_QUEUE_OVERRIDES: dict[str, Any]

def ensure_quorum_queue_compatibility(routing_key: str, queue_name: str, **options: Any) -> dict[str, Any]: ...
