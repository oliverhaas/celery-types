from typing import ClassVar

from celery.bootsteps import Step

class Connection(Step):
    name: ClassVar[str]
