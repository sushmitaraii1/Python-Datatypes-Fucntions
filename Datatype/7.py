# 7. Write a Python function that takes a list of words and returns the length of the
# longest one.


def longest_word_length(list1):
    longest_length = 0
    for word in list1:
        if longest_length < len(word):
            longest_length = len(word)
    return longest_length


sample_word = ['apple','orange','kiwi','pomogranate']

a = longest_word_length(sample_word)


print("The longest word length is {}".format(a))
