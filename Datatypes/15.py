# 15. Write a Python function to insert a string in the middle of a string.
# Sample function and result :
# insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
# insert_sting_middle('{{}}', 'PHP') -> {{PHP}}


def insert_middle(string1,string2):
    n = len(string1)
    return string1[0:int((n / 2))] + string2 + string1[int((n / 2)):]


sample1, sample2 = input("Enter string1 and string2: ").split()

result = insert_middle(sample1,sample2)
print(result)
