import time


def time_tracker(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} is running")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} is completed in {end_time - start_time:.6f} seconds")
        return result
    return wrapper

@time_tracker
def func_1(v1):
    @time_tracker
    def func_2(v2):
        return v1 + v2 ** 2

    return func_2

@time_tracker
def func_3(v3):
    v1 = 10
    func_2 = func_1(v1)
    return func_2(v3)

# Example execution
result = func_3(5)
print("Result:", result)
