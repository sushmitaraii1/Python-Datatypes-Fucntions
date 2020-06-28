# 34. Write a Python script to merge two Python dictionaries.

d1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}
d2 = {8: 64, 9: 81, 10: 100, 11: 121, 12: 144}

d1.update(d2)
print(d1)