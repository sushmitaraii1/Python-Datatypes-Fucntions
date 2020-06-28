# 11. Write a Python program to create a lambda function that adds 15 to a given
# number passed in as an argument, also create a lambda function that multiplies
# argument x with argument y and print the result.


add_num = lambda a: a + 15
sample = int(input("Enter a number: "))
r = add_num(sample)
print(f"The number after adding 15 is {r}.")

mul_num = lambda x, y: x * y
sample1 = int(input("Enter first number: "))
sample2 = int(input("Enter second number: "))

result = mul_num(sample1, sample2)
print(f"The result after multiplying is {result}.")
