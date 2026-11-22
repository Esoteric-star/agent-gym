"""In-memory cache with LRU eviction and time-to-live."""
import time


class TTLCache:
    """A bounded cache.

    TTLCache(maxsize, ttl, clock=time.monotonic)
    - maxsize: int >= 1, maximum number of live entries. ValueError otherwise.
    - ttl: seconds (> 0) an entry lives after it was last set. ValueError otherwise.
    - clock: zero-arg callable returning seconds; injectable for tests.

    Methods:
    - set(key, value): store or overwrite; resets that key's expiry and makes
      it most recently used. If this would exceed maxsize, first drop all
      expired entries, then evict the least recently used entry.
    - get(key, default=None): return the value if present and not expired,
      and mark it most recently used (does NOT extend its expiry). Expired
      entries are removed and default returned.
    - __len__(): number of entries that have not expired.
    - __contains__(key): True if present and not expired (does not affect recency).
    An entry expires when clock() >= time_set + ttl.
    """

    def __init__(self, maxsize, ttl, clock=time.monotonic):
        raise NotImplementedError

    def set(self, key, value):
        raise NotImplementedError

    def get(self, key, default=None):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

    def __contains__(self, key):
        raise NotImplementedError
