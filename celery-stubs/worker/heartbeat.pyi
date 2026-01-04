from typing import Any

class Heart:
    def __init__(
        self,
        timer: Any,
        eventer: Any,
        interval: float | None = None,
    ) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
