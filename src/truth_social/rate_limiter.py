thonimport threading
import time
from typing import Optional

class RateLimiter:
    """
    Simple time-based rate limiter.

    Ensures that calls to `wait()` are spaced out according to the configured
    number of calls per minute.
    """

    def __init__(self, calls_per_minute: int = 60) -> None:
        if calls_per_minute <= 0:
            raise ValueError("calls_per_minute must be positive.")

        self.calls_per_minute = calls_per_minute
        self.min_interval = 60.0 / float(calls_per_minute)
        self._lock = threading.Lock()
        self._last_call: Optional[float] = None

    def wait(self) -> None:
        """
        Block until enough time has passed since the previous call.
        """
        with self._lock:
            now = time.monotonic()
            if self._last_call is None:
                self._last_call = now
                return

            elapsed = now - self._last_call
            remaining = self.min_interval - elapsed
            if remaining > 0:
                time.sleep(remaining)
            self._last_call = time.monotonic()