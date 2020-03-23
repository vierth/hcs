# Return just part a match using groups
import re

# groups are formed with ()
some_html = "<a href='www.google.com'>Google</a>"

result = re.search(r"<a href='(.+)'", some_html)

print(result)
# get just google.com with the group method
print(result.group(1))

my_string = "It occured on pages 336-7."
result = re.search('(\d+)-(\d+)', my_string)
first_number = result.group(1)
second_number = result.group(2)
print(first_number, second_number)
print(result.group(0))

