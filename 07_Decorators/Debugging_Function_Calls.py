
# Problem : Create a decorator to print the function name and values of its arguments everytime the function is called.

# Decorator
def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{key}={value}" for key, value in kwargs.items())
        print(f"Calling : {func.__name__} with Arguments : {args_value} and Key-Value-Arguments : {kwargs_value}")
        result = func(*args, **kwargs)
        return result
    return wrapper



@debug                                      # Decorator
def welocme():
    print("====Welcome====")


@debug                                      # Decorator
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")


# Calling Function
welocme()
greet("Madhav", greeting="Hello")

