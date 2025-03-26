# CHATGPT

class Timer:
    """
    Utility class to measure execution time.

    This class provides a static method `time_wrapper` that acts as a decorator
    to measure the execution time of a function.

    Methods
    -------
    time_wrapper(func)
        Decorator that prints the execution time of the wrapped function.
    """

    @staticmethod
    def time_wrapper(func):
        """
        Decorator that measures and prints the execution time of a function.

        Parameters
        ----------
        func : callable
            The function whose execution time needs to be measured.

        Returns
        -------
        callable
            A wrapped version of `func` that prints execution time.

        Examples
        --------
        >>> import time
        >>> @Timer.time_wrapper
        ... def example_function():
        ...     time.sleep(1)
        ...
        >>> example_function()
        example_function is running
        example_function completed in 1.000x seconds
        """
        def wrapper(*args, **kwargs):
            print(f"{func.__name__} is running")
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"{func.__name__} completed in {end_time - start_time:.4f} seconds")
            return result
        return wrapper
