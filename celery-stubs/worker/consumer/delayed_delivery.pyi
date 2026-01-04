from typing import ClassVar

from celery.bootsteps import Step

class DelayedDelivery(Step):
    name: ClassVar[str]
