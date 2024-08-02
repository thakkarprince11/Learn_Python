
# Create a lamda function to compute the cube of a number.

# this is normal function - lamda function are for one time use and that don't have any name
def cube_number(num):
    return (num ** 3)

result = cube_number(3)
print(result)


# lamda function
cube = lambda num: num ** 3

print(cube(3))
