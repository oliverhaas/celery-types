from typing import ClassVar

from celery.bootsteps import Step

class Events(Step):
    name: ClassVar[str]
