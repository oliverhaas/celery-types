from typing import ClassVar

from celery.bootsteps import Step

class Heart(Step):
    name: ClassVar[str]
