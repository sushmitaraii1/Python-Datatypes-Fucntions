# 25. Write a Python program to check whether all dictionaries in a list are empty or
# not.

my_list1 = [{},{},{}]
my_list2 = [{1,2},{},{}]
print(all(not d for d in my_list1))
print(all(not d for d in my_list2))