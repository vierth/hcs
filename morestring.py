# Some more string stuff:
s = "test string for fun testing"

# find returns -1 if no results:
print(s.find("y"))

# rfind returns the last results
print(s.rfind("s"))

# string slices:
s[0] # first character
s[:10] # first ten characters (index 0 to 9)
s[10:] # characters from ten to the end of teh string
s[10:14] # characters ten to 13
s[-1] # negative numbers count from the end (think length - 1)

# replacing substrings without overwriting
t = s.replace("t", "0")
# save to s to overwrite

# more methods
s.isalnum() # check if is alphanumeric
s.isdecimal() # check if is decimal numbers (alphabetical/punctuation breaks it)
s.isnumeric() # check if it is numeric
s.isalpha() # check if only alphabetical