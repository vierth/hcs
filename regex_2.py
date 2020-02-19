# There are a number of special characters in regular expressions that
# match specific patterns
import re

my_string = "It is now the year 2020"

# if i want to match a number from 0-9
# \d

result = re.search(r'\d', 'It is now the year 2020')
print(result)

# Match anything that is NOT a numbe4
# \D
result_2 = re.search(r'\D', 'It is now the year 2020')
print(result_2)

# \s will match any whitespace
r_3 = re.search(r'\s', my_string)
print(r_3)

#\S will match any NON whitespace
r_4 = re.search(r'\S', my_string)
print(r_4)

# \t will match tab, \n will match a new line character

#\w matches letters, numbers, chinese characters \W doesn't match letters, number etc
r_5 = re.search(r'\w', my_string)
print(r_5)

#. matches everything but a new line character
r_6 = re.search(r'.', my_string)
print(r_6)


#\b will detect a word boundary (#\B will detect at NOT a word boundary)
test_string = 'Will we find friendship or an ocean ship.'
r_7 = re.search(r'\bship', test_string)
print(r_7)

# ?
r_8 = re.search(r'humou?r', "Americans spell it humor.")
print(r_8)

# +
# matches one or more examples of the previous term
result = re.search(r'\d+', my_string)
print(result)

# * match something zero or more times.
r1 = re.search(r'humou*r', "Americans spell it humor")
r2 = re.search(r'humou*r', "Brits spell it humour")
r3 = re.search(r'humou*r', "No one spell it humouuuuuuuuuuur")

print(r1)
print(r2)
print(r3)