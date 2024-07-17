import re

text = "Random String 98 wvsvsvssv MyName123@website.com more text serbdbvesd your_name8-8-8@company.net"
# Stops when it finds the first match
# (a to z thn A-Z)   pattern = re.compile("[a-zA-Z]")
# pattern = re.compile("[a-zA-z0-9]+")
pattern = re.compile("[a-zA-Z0-9\.\-\_]+@[a-zA-Z0-9]+\.[a-zA-Z]+")
# searches for the first match result = pattern.search(text)
result = pattern.findall(text)
print (result)