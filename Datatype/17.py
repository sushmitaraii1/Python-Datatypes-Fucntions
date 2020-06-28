# 17. Write a Python program to multiplies all the items in a list.


def multuple(element):
    product = 1
    for x in element:
        product *= x
    return product


result = multuple([1,2,4,5,6])
print(result)