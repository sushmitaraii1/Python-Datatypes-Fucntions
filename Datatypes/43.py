# 43. Write a Python program to remove an item from a tuple.

tup = ('a', 'b', 'c', 'd', 'e')

# method 1

x = tup[:1] + tup[2:]
print(x)

# method 2

lst = list(tup)
lst.remove("c")
y = tuple(lst)
print(y)
