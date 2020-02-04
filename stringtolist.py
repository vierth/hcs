# You can turn a string into a list of characters easily
s = "This is the fun test string"
list_chars = list(s)

# you can use split to divide according to a substring
list_words = s.split(" ") # splits on whitespace (we will see better ways later)

# you can join a list of strings together with a character:
" ".join(list_words)