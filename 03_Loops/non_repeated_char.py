
# Given a String, find the first non-repeated character

#input_string = "teeter"
input_string = "teeteracdacd"


for char in input_string:
    #print(char)
    if  input_string.count(char) == 1:
        print("Non-repeated first char is : ", char)
