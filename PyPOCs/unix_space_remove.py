import re

# Your original string with a non-breaking space
original_string = "This is a string\u00a0 with\xa0a multiple non-breaking space."
print("length of original_string = ", len(original_string))
print("original_string = ", original_string)                    # it will not appear in print
file = open("original_string.txt", "w")                         # it will appear in file
file.write(original_string)
file.close()


# Using regular expressions to replace all whitespace characters with a space

result_string = re.sub(r'\s', ' ', original_string)
print("length of result_string = ", len(result_string))
print("result_string = ", result_string)
file = open("result_string.txt", "w")
file.write(result_string)
file.close()
