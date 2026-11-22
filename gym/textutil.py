"""Text helpers."""


def slugify(text):
    """Convert text to a URL slug.

    Rules: lowercase; any run of characters that are not a-z or 0-9 becomes a
    single hyphen; no leading or trailing hyphens; empty input returns "".
    Accented Latin letters are reduced to their base letter (e.g. "é" -> "e").
    """
    raise NotImplementedError
