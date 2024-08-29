
# Problem : Write a decorator that measures the time a function takes to execute.

import time

# Decorator
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)              # Executing Function that passed as argument
        end_time = time.time()
        print(f"{func.__name__} ran in {end_time-start_time} time")                       
        return result
    return wrapper


@timer                                              # This means decorating function. Now it will be passed by timer first
def example_function(n):
    time.sleep(n)

example_function(2)                                 # Executing Function for 2 Secs

