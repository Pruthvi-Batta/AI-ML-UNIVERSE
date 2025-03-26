import functools
import time
from typing import List, Union


class PerformanceTracker:
    """
    A decorator class to track function performance and execution time.
    """
    @staticmethod
    def track_performance(func):
        """
        Decorator method to track function performance and execution time.

        Args:
            func (callable): The function to be tracked

        Returns:
            callable: Wrapped function with performance tracking
        """
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"{func.__name__} is running")
            start_time = time.time()

            try:
                result = func(*args, **kwargs)
                return result
            finally:
                end_time = time.time()
                print(f"{func.__name__} completed in {end_time - start_time:.4f} seconds")

        return wrapper

class Calculation:
    """
    A class to represent a single calculation operation.
    Stores input values and calculation result.
    """
    def __init__(self, a: Union[int, float], b: Union[int, float]):
        """
        Initialize a Calculation object.

        Args:
            a (int or float): First operand
            b (int or float): Second operand
        """
        self.a = a
        self.b = b
        self.result = None

    @PerformanceTracker.track_performance
    def calculate(self) -> float:
        """
        Perform calculation: a + b^2

        Returns:
            float: Calculation result
        """
        self.result = self.a + (self.b ** 2)
        return self.result

class CalculationManager:
    """
    Manages multiple calculations and provides retrieval mechanisms.
    """
    def __init__(self):
        """
        Initialize CalculationManager with an empty list of calculations.
        """
        self.calculations: List[Calculation] = []

    def add_calculation(self, a: Union[int, float], b: Union[int, float]) -> Calculation:
        """
        Add a new calculation to the manager.

        Args:
            a (int or float): First operand
            b (int or float): Second operand

        Returns:
            Calculation: Created Calculation object
        """
        calculation = Calculation(a, b)
        calculation.calculate()
        self.calculations.append(calculation)
        return calculation

    def get_calculation_results(self) -> List[float]:
        """
        Retrieve results of all calculations.

        Returns:
            List[float]: List of calculation results
        """
        return [calc.result for calc in self.calculations]

    def get_calculation_by_index(self, index: int) -> Calculation:
        """
        Retrieve a specific calculation by index.

        Args:
            index (int): Index of the calculation

        Returns:
            Calculation: Calculation object at the specified index

        Raises:
            IndexError: If the index is out of range
        """
        return self.calculations[index]

def main():
    """
    Demonstration of CalculationManager functionality.
    """
    # Create a CalculationManager instance
    calc_manager = CalculationManager()

    # Add multiple calculations
    calc_manager.add_calculation(5, 3)
    calc_manager.add_calculation(10, 2)
    calc_manager.add_calculation(7, 4)

    # Retrieve and print all results
    print("\nAll Calculation Results:")
    for result in calc_manager.get_calculation_results():
        print(result)

    # Retrieve a specific calculation
    print("\nSpecific Calculation:")
    specific_calc = calc_manager.get_calculation_by_index(1)
    print(f"Calculation: {specific_calc.a} + {specific_calc.b}^2 = {specific_calc.result}")

if __name__ == "__main__":
    main()