# 6. Write a Python program to find the first appearance of the substring 'not' and
# 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
# substring with 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'

sample = input("Enter a sentence: ")
new_sentence = ""
not_index = sample.find('not')
poor_index = sample.find('poor')


if not_index < poor_index:
    new_sentence += sample[0:not_index] + 'good!'
else:
    new_sentence += sample
print(new_sentence)