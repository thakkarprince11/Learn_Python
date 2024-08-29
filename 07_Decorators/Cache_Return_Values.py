import time
# Problem : Implement a decorator that caches the return value of a function, so that when it's called with the same arguments, the cached value is returned instead of re-executing the function.


# Decorator
def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result =  func(*args)
        cache_value[args] = result
        return result
    return wrapper



@cache                                      # Decorator
def long_running_function(a, b):
    time.sleep(4)
    return a + b


# Executing Function Back to Back
print(long_running_function(11, 7))
print(long_running_function(11, 7))

print(long_running_function(19, 97))
