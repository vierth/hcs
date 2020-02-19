import re

# greedy operators will try to match the longest pattern possible

my_string = "arglebargle!"

result = re.search(r'a.+e', my_string)

print(result)

# to prevent greedy operators from beeing greedy we can use ? after the operator
result = re.search(r'a.+?e', my_string)

print(result)