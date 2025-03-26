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

class Calculator:
    """Performs mathematical calculations."""
    @staticmethod
    @Timer.time_wrapper
    def compute(a, b):
        return a + b ** 2

class CalculationManager:
    """Manages multiple calculations and stores results."""
    def __init__(self):
        self.calculations = []

    @Timer.time_wrapper
    def perform_calculation(self, a, b):
        result = Calculator.compute(a, b)
        self.calculations.append(result)
        return result

    def get_result(self, index):
        if 0 <= index < len(self.calculations):
            return self.calculations[index]
        raise IndexError("Invalid index")

# Example usage
if __name__ == "__main__":
    manager = CalculationManager()
    result1 = manager.perform_calculation(3, 4)
    result2 = manager.perform_calculation(5, 6)
    print("Stored Results:", manager.calculations)
    print("Retrieved Result at index 1:", manager.get_result(1))
