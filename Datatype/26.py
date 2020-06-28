# 26. Write a Python program to insert a given string at the beginning of all items in
# a list.
# Sample list : [1,2,3,4], string : emp
# Expected output : ['emp1', 'emp2', 'emp3', 'emp4']

sample_lst = [1,2,3,4]
sample_str =  'emp'
new_lst = []
for ele in sample_lst:
    new_lst.append(sample_str + str(ele))

print(new_lst)