"""Simple statistics helpers."""


def moving_average(values, window):
    """Return the simple moving average of `values` over `window` items.

    The result has len(values) - window + 1 items. Raise ValueError if
    window < 1 or window > len(values).
    """
    if window < 1:
        raise ValueError("window must be >= 1")
    if window > len(values):
        raise ValueError("window must be <= len(values)")
    out = []
    for i in range(len(values) - window + 1):
        chunk = values[i:i + window]
        out.append(sum(chunk) / window)
    return out
