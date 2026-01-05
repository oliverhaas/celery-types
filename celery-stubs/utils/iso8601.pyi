import re
from datetime import datetime

ISO8601_REGEX: re.Pattern[str]
TIMEZONE_REGEX: re.Pattern[str]

def parse_iso8601(datestring: str) -> datetime: ...
