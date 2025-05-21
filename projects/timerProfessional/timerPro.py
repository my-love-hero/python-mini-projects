import time

class TimerError(Exception):
    """Custom exception for Timer class errors."""
    pass

class Timer:
    def __init__(self, name=None):
        self._start_time = None
        self._end_time = None
        self.name = name

    def start(self):
        """Start a new timer."""
        if self._start_time is not None:
            raise TimerError("Timer is already running.")
        self._start_time = time.perf_counter()
        self._end_time = None
        if self.name:
            print(f"[{self.name}] Timer started.")

    def stop(self):
        """Stop the timer, and report the elapsed time."""
        if self._start_time is None:
            raise TimerError("Timer is not running.")
        self._end_time = time.perf_counter()
        elapsed_time = self._end_time - self._start_time
        self._start_time = None
        if self.name:
            print(f"[{self.name}] Timer stopped. Elapsed: {elapsed_time:.6f} seconds.")
        return elapsed_time

    def elapsed(self):
        """Check elapsed time without stopping the timer."""
        if self._start_time is None:
            raise TimerError("Timer is not running.")
        return time.perf_counter() - self._start_time

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *args):
        self.stop()

# Example usage
if __name__ == "__main__":
    print("Manual Timer:")
    timer = Timer("Manual")
    timer.start()
    time.sleep(1.2)
    timer.stop()

    print("\nContext Manager Timer:")
    with Timer("Block"):
        time.sleep(1.5)
