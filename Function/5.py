# 5. Write a Python function to calculate the factorial of a number (a non-negative
# integer). The function accepts the number as an argument.


def factorial(num):
    p = 1
    for i in range (1,num+1):
        p *= i
    return p


sample = int(input("Enter a number: "))

print(f"The factorial of {sample} is {factorial(sample)}.")