from typing import ClassVar

from celery.bootsteps import Step

class Agent(Step):
    name: ClassVar[str]
