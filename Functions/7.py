# 7. Write a Python function that accepts a string and calculate the number of
# upper case letters and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12


def case_count(string):
    upper_count = 0
    lower_count = 0
    for i in string:
        if i.isupper():
            upper_count += 1
        elif i.islower():
            lower_count +=1
    return upper_count,lower_count


sample = input("Enter a string: ")
u,l = case_count(sample)
print(f"The uppercase count is {u} and lower case cont is {l}.")

