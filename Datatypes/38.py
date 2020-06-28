# 38. Write a Python program to remove a key from a dictionary.
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

key_input = int(input("Enter key to remove: "))
try:
     d.pop(key_input)
except KeyError:
    print("Key not found")

print(d)