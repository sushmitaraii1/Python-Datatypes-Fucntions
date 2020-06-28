# 11. Write a Python program to count the occurrences of each word in a given
# sentence.

sample = input("Enter a sentence: ").upper()
word_count = {}
word_list = sample.split()

for word in word_list:
    if word not in word_count:
        word_count[word] = 1
    else:
        word_count[word] += 1
print(word_count)
