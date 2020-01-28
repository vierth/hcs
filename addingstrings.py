# Adding strings together (concatenation) is simple:

one_string = "This is a string"
two_string = "Another string"

three_string = one_string + two_string

print(three_string)

# This will look a bit better with a space:

four_string = one_string + " " + two_string

print(four_string)

# adding numbers, when they are strings, will behave like language information
# and not like numerical
print("1234" + "5678")

# we can multiply them too
print("1234"*4)