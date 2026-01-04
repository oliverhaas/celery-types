from typing import ClassVar

from celery.bootsteps import Step

class Tasks(Step):
    name: ClassVar[str]
