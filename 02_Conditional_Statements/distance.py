

distance = int(input("Please enter distance : "))

if distance < 3:
    transport = "Walk"
elif distance <= 15:
    transport = "Bike"
elif distance > 15:
    transport = "Car"
else :
    transport = "Please enter valid distance"


print("AI recommends you transport of", transport)


