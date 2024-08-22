# 
username = "Porsche"

def func():
    username = "Rivian"
    print(username)


def funcTwo():
    #username = "Rivian"
    print(username)


print(username)
func()                  # Calling Function
funcTwo()               # Calling Function


# 
x = 99

def funThree(y):
    z = x + y
    return z

result = funThree(1)             # Calling Function 
print(result)


# 
i = 11

def fun4():
    global i                    # Not Recommended to use
    i = 7

fun4()                          # Calling Function
print(i)


#
t = 108

def f1():
    t = 21
    def f2():
        print(t)
    f2()                        # Calling Function

f1()                            # Calling Function


def f3():
    #t = 21
    def f4():
        print(t)
    f4()                        # Calling Function

f3()                            # Calling Function

# Closure
def f5():
    t = 21
    def f6():
        print(t)
    return f6                       # Returning f6 Function Reference

newResult = f5()                            # Calling Function
print(newResult)
newResult()                                 # Now you are Calling f6 Function


def f7():
    #t = 21
    def f8():
        print(t)
    return f8                       # Returning f8 Function Reference

newResult2 = f7()                            # Calling Function
print(newResult2)
newResult2()                                 # Now you are Calling f8 Function

 
def f9(num):
    def actual(digit):
        return digit ** num
    return actual

closure = f9(2)                            # Closure also know as Factory Function
lexical = f9(3)

power2 = closure(5)
power3 = lexical(5)
print(power2)
print(power3)