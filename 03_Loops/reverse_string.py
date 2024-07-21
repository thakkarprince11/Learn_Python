
# Reverse string using a loop


input_string = input("Enter a String : ")

reversed_string = ""


for char in input_string:
    reversed_string = char + reversed_string

print(reversed_string)
