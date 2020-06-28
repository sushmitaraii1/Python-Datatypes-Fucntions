# 8. Write a Python function that takes a list and returns a new list with unique
# elements of the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]


def unique(lst):
    lst1 = []
    for item in lst:
        if item not in lst1:
            lst1.append(item)
    return lst1


sample_list = [1, 2, 3, 3, 3, 3, 4, 5, 6666, 6666]

print(unique(sample_list))
