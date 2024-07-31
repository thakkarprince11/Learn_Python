
# importing math
import math


# Create a function that returns both the area and circumference of a circle given its radius.


# this will return only 1 value
def circle_stats(radius):
    return math.pi * (radius ** 2)
    print("this will not execute")

print('Area of circle is : ', circle_stats(3))

# return multiple value
def circle_area_circ(radius):
    area = math.pi * (radius ** 2)
    circumference = 2 * math.pi * radius
    return area, circumference

print(circle_area_circ(3))

a, c = circle_area_circ(3)                  # Hold it in variables a and c

print('Area : ', a)
print('Circumference : ', c)


# round figure value
print('Area : ', round(a,2))
print('Circumference : ', round(c,2))
