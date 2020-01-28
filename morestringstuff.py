test_string = "this is a STRING to play around with."

# we can measure how long a string is with len()
print(len(test_string))

# we can make it all upper case:
print(test_string.upper())

# we can make it all lower case:
print(test_string.lower())

# we can capitalize it:
print(test_string.capitalize())

# we can put it in title case:
print(test_string.title())

# we can replace substrings (here we replace all the is with os):
print(test_string.replace("i", "o"))

# we can find the index of a substring (this only finds the first example)
print(test_string.find("i"))

# we get -1 if it doesn't find it:
print(test_string.find("z"))