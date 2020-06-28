# 4. Write a Python program to reverse a string.
# Sample String : "1234abcd"
# Expected Output : "dcba4321"


def rev_string(string):
    return string[::-1]


sample = input("Enter a string : ")

print(rev_string(sample))