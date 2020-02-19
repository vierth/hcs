# It is easy to search for the literal version of a special character
import re

# you do this by escaping the character with a \
results = re.findall(r"\[.+\]", "It happened in [1980].")
print(results)

# \.
# \* 
# \+
# \\
# \[