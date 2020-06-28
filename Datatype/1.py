
# 1. Write a Python program to count the number of characters (character
# frequency) in a string.


sample = input('Enter a string: ')
count = {}
for character in sample:
    if character not in count:
        count[character] = 1
    else:
        count[character] += 1
print(count)

