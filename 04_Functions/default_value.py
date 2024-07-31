
# Write a function that greets a user. if no name is provided, it should greet with a default name.


def greet(name):
    return "Hello, " + name + "!"

print(greet("AS"))

# default parameter
def default_greet(name = "User"):
    return "Hello, " + name + "!"

print(default_greet())
print(default_greet("AS"))
