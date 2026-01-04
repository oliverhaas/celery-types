from typing import ClassVar

from celery.bootsteps import Step

class Control(Step):
    name: ClassVar[str]
