# 12. Write a Python program to create a function that takes one argument, and
# that argument will be multiplied with an unknown given number.


def mul(n):
    return lambda x: x * n

result = mul(2)
print(f'Multiplying number with 2 is {result(15)}.')
