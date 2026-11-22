"""Text helpers."""

import re
import unicodedata


def slugify(text):
    """Convert text to a URL slug.

    Rules: lowercase; any run of characters that are not a-z or 0-9 becomes a
    single hyphen; no leading or trailing hyphens; empty input returns "".
    Accented Latin letters are reduced to their base letter (e.g. "é" -> "e").
    """
    if not text:
        return ""
    
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    
    text = text.lower()
    
    text = re.sub(r"[^a-z0-9]+", "-", text)
    
    text = text.strip("-")
    
    return text
