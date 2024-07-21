

# Recommend a type of pet food based on pet's species and age. (e.g. Dog: < 2years - Puppy Food, Cat > 5years - Senior Cat Food).

pet = input("Enter your pet type e.g. Cat or Dog : ").lower()
age = int(input("Enter age of pet : "))

if (pet == "dog"):
    if (age < 2):
        food = "Puppy Food"
    elif (age >= 2):
        food = "Adult Dog Food"
elif (pet == "cat"):
    if (age <= 5):
        food = "Junior Cat Food"
    elif (age > 5):
        food = "Senior Cat Food"
else:
    print("Please enter valid Pet type and Age")
    exit()

print("Recommended food is : ", food)


