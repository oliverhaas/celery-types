from celery.app.base import Celery

class AMQP:
    def __init__(self, app: Celery) -> None: ...
