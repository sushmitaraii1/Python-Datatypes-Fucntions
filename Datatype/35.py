# 35. Write a Python program to iterate over dictionaries using for loops.

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
for index,value in d.items():
    print("Key is {} and value is {}.".format(index,value))