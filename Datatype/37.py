# 37. Write a Python program to multiply all the items in a dictionary.

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

product = 1

for itm in d:
    product *= d[itm]

print(product)