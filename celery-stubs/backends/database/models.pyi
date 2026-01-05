from datetime import datetime

class Task:
    id: int | None
    task_id: str
    status: str
    result: bytes | None
    date_done: datetime | None
    traceback: str | None
    name: str | None
    args: bytes | None
    kwargs: bytes | None
    worker: str | None
    retries: int | None
    queue: str | None

class TaskSet:
    id: int | None
    taskset_id: str
    result: bytes | None
    date_done: datetime | None
