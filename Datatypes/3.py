# 3. Write a Python program to get a string from a given string where all
# occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'

sample = input("Enter a string: ")
new_word = sample[0]
first_char = sample[0]
for i in range(1, len(sample)):
    if sample[i] == first_char:
        new_word += '$'
    else:
        new_word += sample[i]
print(new_word)