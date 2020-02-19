# we can replace values using regular expresions
import re

my_string = "This has a few        spaces.      "
print(my_string)
my_string = re.sub(r'\s+', " ", my_string)
print(my_string)

my_string_2 = "Double.  Spaces.  Are.  Wrong."
my_string_2 = re.sub(r'\.\s{2}', ". ", my_string_2)
print(my_string_2)

# Change all dogs and cats to kapow!
m2 = "cats and dogs and logs are dogs"
m2 = re.sub(r'cats|dogs', 'kapow!', m2)
print(m2)

# add some markup to a text file
my_string_3 = 'Oh Captain, my Captain, are you a General?'

my_string_3 = re.sub(r'(Captain|General)', "<title>\g<1></title>", my_string_3)
print(my_string_3)
