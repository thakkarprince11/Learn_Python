

# Calculate the sum of even numbers up to given number n.

n = int(input("Enter a Number : "))

sum_even = 0
count_even = 0

# range 2nd parameter exclusive so to make it inclusive add +1
for i in range(1, n + 1):
    if i % 2 == 0:
        sum_even = sum_even + i
        count_even = count_even + 1

print("Sum of event numbers is : ", sum_even)
print("Count of even numbers is : ", count_even)



