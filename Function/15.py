# 15. Write a Python program to filter a list of integers using Lambda.


lst = [1, 5, 6, 4, 8, 5, 6, 9, 5, 3, 5, 9]

sorted_list = list(filter(lambda x:x%2==0,lst))
print("The even numbers from list are: ")
print(sorted_list)