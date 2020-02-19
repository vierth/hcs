import re

# you can create a character set with []
# [abc] this will match a or b or c
result = re.findall(r'[abc]+', "do you run this place?")
print(result)

# [a-e] will match a,b,c,d,e
# [a-zA-Z] if we want to match any alphabetical character
# [0-9] will match 0 to 9 (equals \d)
# [a-zA-Z0-9]
# [^a]
result = re.findall(r'[^a^o]+', "do you run this place?")
print(result)

