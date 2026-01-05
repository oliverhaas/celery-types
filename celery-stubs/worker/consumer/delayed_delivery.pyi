from typing import Any, ClassVar

from celery.bootsteps import Step

__all__ = ("DelayedDelivery",)

class DelayedDelivery(Step):
    name: ClassVar[str]

    def include_if(self, c: Any) -> bool: ...
    def start(self, c: Any) -> None: ...
