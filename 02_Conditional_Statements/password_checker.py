

password = input("Please enter your password : ")

if len(password) < 6:
    strength = "Weak"
elif len(password) <= 10:
    strength = "Medium"
elif len(password) > 10:
    strength = "Strong"
else :
    strength = "Please enter valid password"

print("Your password is ", strength)



