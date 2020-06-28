# 14. Write a Python function to create the HTML string with tags around the
# word(s).
# Sample function and result :
#
# add_tags('i', 'Python') -> '<i>Python</i>'
# add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'


def add_tags(tag, string):
    print("<" + tag + ">" + string + "</" + tag + ">")
    return "<" + tag + ">" + string + "</" + tag + ">"


tag_input, string_input = input("Enter tag and word(s) : ").split()

result = add_tags(tag_input, string_input)
print(result)
