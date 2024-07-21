
# Print the multiplication table for given number up to 10, but skip the fifth iteration

number = int(input("Enter a number : "))


for i in range(1, 11):
    if i == 5:
        continue
    print(number, "X", i, "=", number*i)
    




