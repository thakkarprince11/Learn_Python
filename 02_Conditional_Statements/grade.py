# assign grade based on score

score = int(input("Enter score : "))

if score > 100:
    print("Please Enter score between 0 and 100")
    exit()                                          # stop execution here if score is above 100


if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"


print("Grade : ", grade)