# 10. Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]


def even_check(lst):
    lst1 = []
    for item in lst:
        if (item%2 == 0):
            lst1.append(item)
    return lst1


sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9,24,66]

print(even_check(sample_list))