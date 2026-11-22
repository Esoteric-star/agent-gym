"""UK date helpers."""
from datetime import date


def parse_uk_date(text):
    """Parse a UK-format date string 'DD/MM/YYYY' into a datetime.date.

    Leading/trailing whitespace is ignored. Raise ValueError on bad input.
    """
    parts = text.strip().split("/")
    if len(parts) != 3:
        raise ValueError(f"not a UK date: {text!r}")
    day, month, year = (int(p) for p in parts)
    return date(year, month, day)
