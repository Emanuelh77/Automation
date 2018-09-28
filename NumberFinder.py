import re

message = "Call me at my office line 208-111-1111 or my personal number 208-444-4444"

#re - regular expressions
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #\d is for decimal
print(phoneNumRegex.findall(message)) #prints all instances of the regex object

m = "hello hello hello hello hello hello"
mRegex = re.compile(r'hello')
find = mRegex.findall(m)
print(find)
