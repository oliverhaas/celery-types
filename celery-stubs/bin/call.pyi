from typing import Any

import click

def call(ctx: click.Context, name: str, **kwargs: Any) -> Any: ...
