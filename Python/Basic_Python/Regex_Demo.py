#Python Regular Expression::

import re

text_data = "The rain in Spain"

rs = re.search("^The.*Spain$", text_data)

print(rs)
print(rs.start())   #position of first match
print(rs.end())

rs = re.findall("in", text_data)  #get a list of all matching values
print(rs)

rs = re.search("\s", text_data)  #find the first white space
print(rs.start())