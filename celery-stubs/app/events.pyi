from celery.app.base import Celery

class Events:
    def __init__(self, app: Celery | None = ...) -> None: ...
