# ticket price based on age - if age is 18 and 18+ then 12$ and below 18 is 8$. but on Wednesday everyone gets discount of 2$. 


age = int(input("Enter age : "))
day = input("Enter a day i.e. Mon, Tue, Wed, ..., Sun: ")

# short syntax
price = 12 if age >= 18 else 8 

if day == "Wed" :
    price = price - 2

print("Ticket price for you is $",price)

