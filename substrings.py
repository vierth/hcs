# We can use square brackets to access different parts of a string
test_string = "Let's get different parts of this string!"

# This returns the first character of the string (note that this is the 
# character at index 0 (not 1))
first_char = test_string[0]
print(first_char)

# this returns the second character:
second_char = test_string[1]
print(second_char)

# note that I can call the variables anything, but I should be sensible. This
# works but is not a great idea:
third_char = test_string[1]
print(third_char)

# we can get slices of the string using a colon in the square brackets. the 
# first number is where to start, and the second is where to stop (but does not
# include the character at the second number, here the sixth character)
chars_two_to_five = test_string[1:5]
print(chars_two_to_five)

# If we don't include anything to the left of the colon it will start from the
# beginning of the string
chars_one_to_five = test_string[:5]
print(chars_one_to_five)

# if we don't include anything to the right, it will go to the end:
chars_six_to_end = test_string[5:]
print(chars_six_to_end)