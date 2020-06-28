# 13. Write a Python program that accepts a comma separated sequence of words
# as input and prints the unique words in sorted form (alphanumerically).
# Sample Words : Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white


sample = input("Enter a comma separated word sequence: ")
new_list = []
word_list = sample.split(',')
for word in word_list:
    if word not in new_list:
        new_list.append(word)
new_list.sort()
print(new_list)