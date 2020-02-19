# We can match things multiple times with the * and the plus
# but we can get more specific than that
import re

# {3} to match somethign excatly 3 times
result = re.search(r'a{3}', "Will we match a or aaa?")
print(result)

# {1, 4}will match at least once but no more than four times

# {, 4} this will match 0 to 4 times

# {4, } Match four or ore times

r'\d{3}-\d{3}-\d{4}'