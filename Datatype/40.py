# 40. Write a Python program to add an item in a tuple.

x = (2,3,5,6,4,7)

# Method 1
x += (9,)
print(x)
# Mehtod 2
y = x[:3] + (12,) + x[:3]
print(y)
# Method 3
z = list(x)
z.append(88)
a = tuple(z)
print(a)