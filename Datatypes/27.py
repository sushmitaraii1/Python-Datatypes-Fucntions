# 27. Write a Python program to replace the last element in a list with another list.
# Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
# Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]

sample1 = [1, 3, 5, 7, 9, 10]
sample2 = [2, 4, 6, 8]

result = sample1[:-1] + sample2
print(result)