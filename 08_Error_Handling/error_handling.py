

file = open('first.txt', 'w')

# try catch finally - Error Handling
try:
    file.write('Radha Krishn')
finally:
    file.close()

# Now Python has New Syntax to Handle File
with open('second.txt', 'w') as file_new:
    file_new.write('Radhe Radhe')

