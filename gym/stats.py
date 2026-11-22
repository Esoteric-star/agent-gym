"""Simple statistics helpers."""
from collections import deque


def moving_average(values, window):
    """Return the simple moving average of `values` over `window` items.

    The result has len(values) - window + 1 items. Raise ValueError if
    window < 1 or window > len(values).
    """
    iterator = iter(values)
    try:
        first = next(iterator)
    except StopIteration:
        values_len = 0
    else:
        values_list = [first]
        values_list.extend(iterator)
        values = values_list
        values_len = len(values)

    if window < 1:
        raise ValueError("window must be >= 1")
    if window > values_len:
        raise ValueError("window must be <= len(values)")
    if values_len == 0:
        return []

    out = []
    window_deque = deque()
    current_sum = 0.0

    for value in values:
        window_deque.append(value)
        current_sum += value
        if len(window_deque) == window:
            out.append(current_sum / window)
            current_sum -= window_deque.popleft()

    return out
