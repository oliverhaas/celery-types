from typing import ClassVar

from celery.bootsteps import Step

class Gossip(Step):
    name: ClassVar[str]
