# Suggest an activity based on Weather (eg. Sunny-go for walk, Rainy-read a book, Snowy-build a snowman)

weather = input("Enter weather condition : ").lower()

if weather == "sunny":
    activity = "Go for a Walk"
elif weather == "rainy":
    activity = "Read a Book"
elif weather == "snowy":
    activity = "Build a Snowman"
else:
    print("Please enter correct weather condition")
    exit()

print(activity)
