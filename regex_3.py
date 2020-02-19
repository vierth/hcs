# the re library contains a few different ways of finding alle xamples of something
import re

my_string = 'In 1954 I found 28 crumptes inside the house at 11 County Road.'

# get a list of all matches to the patern
res = re.findall(r'\d+', my_string)

# get the match objects of all matches to the patern
res = re.finditer(r'\d+', my_string)

for r in res:
    print(r.start(), r.group())