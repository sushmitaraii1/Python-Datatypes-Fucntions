# 3. Write a Python function to multiply all the numbers in a list.
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336


def product(lst):
    m = 1
    for elements in lst:
        m *= elements
    return m


sample_list = [8, 2, 3, 1, 7]
print(f"Ths sum of items in list is {product(sample_list)}.")