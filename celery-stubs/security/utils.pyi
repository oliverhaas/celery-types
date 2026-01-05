from collections.abc import Iterator
from contextlib import contextmanager
from typing import Any

__all__ = ("get_digest_algorithm", "reraise_errors")

def get_digest_algorithm(digest: str) -> Any: ...
@contextmanager
def reraise_errors(
    msg: str = "{0!r}", errors: tuple[type[Exception], ...] | None = None
) -> Iterator[None]: ...

class SecurityError(Exception): ...
