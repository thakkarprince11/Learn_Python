
# Write a function that takes variable number of arguments and returns their sum.

# *args function that can 1 to many parameters
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2))
print(sum_all(1, 2, 3))
print(sum_all(1, 2, 3, 4))
print(sum_all(1, 2, 3, 4, 5))


print('------------------------------------')

# Inner Working - *args function
def summ_all(*args):
    print(*args)
    return sum(args)

print(summ_all(1, 2))
print(summ_all(1, 2, 3))
print(summ_all(1, 2, 3, 4))
print(summ_all(1, 2, 3, 4, 5))

print('------------------------------------')

def summ_alll(*args):
    print(args)
    return sum(args)

print(summ_alll(1, 2))
print(summ_alll(1, 2, 3))
print(summ_alll(1, 2, 3, 4))
print(summ_alll(1, 2, 3, 4, 5))

print('------------------------------------')

def sum_all_mult(*args):
    print(args)
    for i in args:
        print(i * 8)
    return sum(args)

print(sum_all_mult(1, 2))
print(sum_all_mult(1, 2, 3))
print(sum_all_mult(1, 2, 3, 4))
print(sum_all_mult(1, 2, 3, 4, 5))
