from collections.abc import Callable, Sequence
from typing import Any

import click

from celery.app.base import Celery

class CeleryOption(click.Option): ...
class CeleryCommand(click.Command):
    app: Celery | None
    def __init__(
        self,
        name: str | None = None,
        params: Sequence[click.Parameter] | None = None,
        **kwargs: Any,
    ) -> None: ...
class CeleryDaemonCommand(CeleryCommand): ...
class CLIContext:
    app: Celery
    def __init__(self, app: Celery | None = None, **kwargs: Any) -> None: ...
class CLI(click.MultiCommand):
    def list_commands(self, ctx: click.Context) -> list[str]: ...
    def get_command(self, ctx: click.Context, name: str) -> click.Command | None: ...

def handle_preload_options(f: Callable[..., Any]) -> Callable[..., Any]: ...
