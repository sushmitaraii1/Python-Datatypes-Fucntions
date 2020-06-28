# 16. Write a Python program to square and cube every number in a given list of
# integers using Lambda.

lst = [1, 5, 6, 4, 8, 5, 6, 9, 5, 3, 5, 9]
print(lst)
print("After squaring items.")
square = list(map(lambda x:x**2,lst))
print(square)
print("After cubing items.")
cube = list(map(lambda x:x**3,lst))
print(cube)