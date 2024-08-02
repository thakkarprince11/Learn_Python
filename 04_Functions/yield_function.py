
# Write a generator function that yields even numbers up to a specified limit.

def even_generator(limit):
    for i in range(2, limit + 1, 2):
        return i

print(even_generator(20))               # returns only one value 2

print("==============================")

# this will return list - but that we don't want 
def even_generator_one(limit):
    li = []
    for i in range(2, limit + 1, 2):
        li.append(i)
    return li

print(even_generator_one(20))

print("=============Yield=================")

# yield - stores memory and state of the function and returns value after that state
def even_generator_two(limit):
    for i in range(2, limit + 1, 2):
        yield i

for i in even_generator_two(10):
    print(i)
 
