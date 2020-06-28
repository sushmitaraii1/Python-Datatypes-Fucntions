# 2. Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20


def summation(lst):
    return sum(lst)


sample_list = [8, 2, 3, 0, 7]
print(f"Ths sum of items in list is {summation(sample_list)}.")
