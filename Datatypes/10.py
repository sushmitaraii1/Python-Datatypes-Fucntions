# 10. Write a Python program to remove the characters which have odd index
# values of a given string.
new_str = ""

sample = input("Enter a string: ")
for i in range(0,len(sample)):
    if i%2 == 0:
        new_str += sample[i]

print(new_str)