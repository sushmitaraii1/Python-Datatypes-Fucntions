# 13. Write a Python program to sort a list of tuples using Lambda.

lst = [(2,1),(5,6),(6,3),(8,77)]
print(lst)
print("After sorting")
lst.sort(key=lambda x : x[0])
print(lst)