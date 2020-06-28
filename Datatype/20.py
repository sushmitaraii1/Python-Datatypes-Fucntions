# 20. Write a Python program to count the number of strings where the string
# length is 2 or more and the first and last character are same from a given list of
# strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2


lst = []
word_count = 0

n = int(input("Enter number of elements : "))


for i in range(0, n):
    element = input("Enter " + str(i) + " element of list: ")

    lst.append(element)

for words in lst:
    if len(words)>2 and words[0]==words[-1]:
        word_count +=1
print(word_count)
