
# Find factorial using a WHILE loop.


number = int(input("Enter a Number: "))
num = number

factorial = 1


while number > 0:
    factorial = factorial * number
    number = number - 1

print(f"Factorial of {num} is : ", factorial)

