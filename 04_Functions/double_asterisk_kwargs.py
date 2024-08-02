
# Create a function that accepts any number of keyword arguments and prints them in the format key:value.


# Normal Function
def print_kwargs(name, power):
    print("Name : ", name, "Power : ", power)

print_kwargs(name="Shaktiman", power="Laser")
print_kwargs(power="Laser", name="Shaktiman")


print("=================================")

# **kwargs function
def heros(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

heros(name="Shaktiman", power="Laser")
print("---------------------------")
heros(power="Laser", name="Shaktiman")
print("---------------------------")
heros(power="Laser", name="Shaktiman", enemy="Dr. Jackal")
