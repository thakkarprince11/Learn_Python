

# Check if all elements in list are unique, if duplicate is found, exit the loop and print the duplicate.

items = ["apple", "banana", "orange", "apple", "mango"]

unique_item = set()         # set only take unique values

for item in items:
    if item in unique_item:
        print("Duplicate : ", item)
        break
    unique_item.add(item)
