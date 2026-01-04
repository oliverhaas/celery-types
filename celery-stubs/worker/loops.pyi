from collections.abc import Callable, Iterator
from typing import Any

def asynloop(
    obj: Any,
    connection: Any,
    consumer: Any,
    blueprint: Any,
    hub: Any,
    qos: Any,
    heartbeat: float,
    clock: Any,
    hbrate: float = 2.0,
    RUN: int = ...,
) -> None: ...
def synloop(
    obj: Any,
    connection: Any,
    consumer: Any,
    blueprint: Any,
    hub: Any,
    qos: Any,
    heartbeat: float,
    clock: Any,
    hbrate: float = 2.0,
    RUN: int = ...,
) -> None: ...
