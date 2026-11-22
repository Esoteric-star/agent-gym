"""In-memory cache with LRU eviction and time-to-live."""
import time
from collections import OrderedDict


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
        if not isinstance(maxsize, int) or maxsize < 1:
            raise ValueError("maxsize must be an integer >= 1")
        if ttl <= 0:
            raise ValueError("ttl must be greater than 0")
        self._maxsize = maxsize
        self._ttl = ttl
        self._clock = clock
        self._data = OrderedDict()
        self._expiry = {}

    def _is_expired(self, key):
        return self._clock() >= self._expiry[key]

    def _cleanup_expired(self):
        expired_keys = [key for key in self._data if self._is_expired(key)]
        for key in expired_keys:
            del self._data[key]
            del self._expiry[key]

    def set(self, key, value):
        if key in self._data:
            del self._data[key]
        self._data[key] = value
        self._expiry[key] = self._clock() + self._ttl
        self._data.move_to_end(key)
        if len(self._data) > self._maxsize:
            self._cleanup_expired()
            while len(self._data) > self._maxsize:
                oldest_key = next(iter(self._data))
                del self._data[oldest_key]
                del self._expiry[oldest_key]

    def get(self, key, default=None):
        if key not in self._data:
            return default
        if self._is_expired(key):
            del self._data[key]
            del self._expiry[key]
            return default
        self._data.move_to_end(key)
        return self._data[key]

    def __len__(self):
        self._cleanup_expired()
        return len(self._data)

    def __contains__(self, key):
        if key not in self._data:
            return False
        if self._is_expired(key):
            del self._data[key]
            del self._expiry[key]
            return False
        return True
