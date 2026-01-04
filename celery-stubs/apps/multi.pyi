from collections.abc import Sequence
from typing import Any

class Cluster:
    name: str
    nodes: list[Node]

    def __init__(
        self,
        nodes: list[str],
        cmd: str | None = None,
        env: dict[str, str] | None = None,
        on_stopping_preamble: Any | None = None,
        on_send_signal: Any | None = None,
        on_still_waiting_for: Any | None = None,
        on_still_waiting_progress: Any | None = None,
        on_still_waiting_end: Any | None = None,
        on_node_start: Any | None = None,
        on_node_restart: Any | None = None,
        on_node_shutdown_ok: Any | None = None,
        on_node_status: Any | None = None,
        on_node_signal: Any | None = None,
        on_node_signal_dead: Any | None = None,
        on_node_down: Any | None = None,
        on_child_spawn: Any | None = None,
        on_child_signalled: Any | None = None,
        on_child_failure: Any | None = None,
    ) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def stopwait(self) -> None: ...
    def restart(self) -> None: ...
    def kill(self) -> None: ...

class Node:
    name: str
    argv: Sequence[str]
    expander: Any
    pid: int | None

    def __init__(
        self,
        name: str,
        argv: Sequence[str] | None = None,
        expander: Any | None = None,
        extra_args: Sequence[str] | None = None,
    ) -> None: ...
    def alive(self) -> bool: ...
    def send(self, sig: int) -> bool: ...
    def start(self, **kwargs: Any) -> int: ...
    def stop(self) -> None: ...
    def stop_and_wait(self) -> None: ...
