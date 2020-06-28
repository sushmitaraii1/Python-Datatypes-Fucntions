# 8. Write a Python program to remove the n
# th
# index character from a nonempty
#
# string.
new_str = ""
sample = input("Enter a non-empty string: ")

n = int(input("Enter index for character to remove: "))

new_str += sample[:n] + sample[n+1:]

print(new_str)

