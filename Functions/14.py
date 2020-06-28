# 14. Write a Python program to sort a list of dictionaries using Lambda.

dict1 = [{"name": "Tom", "age": 10},
         {"name": "Mark", "age": 5},
         {"name": "Pam", "age": 7}]

sort_dict = sorted(dict1,key=lambda x: x["age"])
print(sort_dict)
