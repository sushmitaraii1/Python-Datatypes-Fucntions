# 18. Write a Python program to check whether a given string is number or not
# using Lambda.
from typing import Any, Callable

sample = input("Enter a number: ")
sample = sample.replace('.', '1')
sample = sample.replace('-', '0')

num_or_not = lambda x: x.isdigit()

if num_or_not(sample):
    print("Given string is a number.")
