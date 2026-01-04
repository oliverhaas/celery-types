from typing import ClassVar

from celery.bootsteps import Step

class Mingle(Step):
    name: ClassVar[str]
