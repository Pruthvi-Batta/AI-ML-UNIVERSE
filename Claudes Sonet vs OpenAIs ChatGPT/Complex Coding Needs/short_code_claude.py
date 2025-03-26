import functools
import time


def timing_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} is running")
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()
        print(f"{func.__name__} is completed in {end_time - start_time:.4f} seconds")

        return result
    return wrapper

@timing_decorator
def func_1(v1):
    def func_2(v2):
        return v2 ** 2

    return func_2

@timing_decorator
def func_3(v3):
    # Using func_1 with v1 = 10
    inner_func = func_1(10)

    # Using func_2 (inner function) with v3 as the argument
    return inner_func(v3)

# Demonstration
def main():
    # Test func_1
    f1 = func_1(5)

    # Test func_2 via func_1
    result_f2 = f1(4)
    print(f"func_2 result: {result_f2}")

    # Test func_3
    result_f3 = func_3(3)
    print(f"func_3 result: {result_f3}")

if __name__ == "__main__":
    main()