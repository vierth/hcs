'''
Regular expresssions let us serach for pattterns in text.
'''

import re

my_string = 'Hello, how are you?'

# search for a pattern in the string using regular expressions
result = re.match(r'Hello', my_string)

# print where the match starts
print(result.start())

# print where the match ends
print(result.end())

#print both at the same time
print(result.span())


