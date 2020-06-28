# 22. Write a Python program to remove duplicates from a list.

lst = []
lst1 = []
n = int(input("Enter number of elements : "))


for i in range(0, n):
    element = input("Enter " + str(i) + " element of list: ")

    lst.append(element)


for i in lst:
    if i not in lst1:
        lst1.append(i)
print(lst1)


