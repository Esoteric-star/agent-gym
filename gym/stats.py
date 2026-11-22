"""Simple statistics helpers."""


def moving_average(values, window):
    """Return the simple moving average of `values` over `window` items.

    The result has len(values) - window + 1 items. Raise ValueError if
    window < 1 or window > len(values).
    """
    values = list(values)
    if window < 1:
        raise ValueError("window must be >= 1")
    if window > len(values):
        raise ValueError("window must be <= len(values)")
    out = []
    window_sum = sum(values[:window])
    out.append(window_sum / window)
    for i in range(window, len(values)):
        window_sum += values[i] - values[i - window]
        out.append(window_sum / window)
    return out
