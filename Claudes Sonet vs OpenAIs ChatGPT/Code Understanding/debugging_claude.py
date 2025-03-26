#claude

import time


class Timer:
    """Utility class to measure execution time."""

    @staticmethod
    def time_wrapper(func):
        def wrapper(*args, **kwargs):
            print(f"{func.__name__} is running")
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"{func.__name__} completed in {end_time - start_time:.4f} seconds")
            return result
        return wrapper