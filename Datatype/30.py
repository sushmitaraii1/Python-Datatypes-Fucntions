# 30. Write a Python script to check whether a given key already exists in a
# dictionary.
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

sample = int(input("Enter int key to check: "))
if sample in d:
    print("Key is present.")
else:
    print("Key is not present")