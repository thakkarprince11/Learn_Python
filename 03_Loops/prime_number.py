
# Check if number is prime number - prime number is that can only divided by itself (e.g. 2, 3, 5, 7, 11).


number = int(input("Enter a Number : "))

is_prime = True

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            is_prime = False
            break

if is_prime :
    print(number, " is a Prime Number")
else:
    print(number, "is NOT a Prime Number")
