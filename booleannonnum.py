# Are two strings the same?
"a" == "b" # False

print ("a" is "a") # True

a = ["hello"]
b = ["hello"]

print(a == b) # True

print(a is b) # False 

print(id(a), id(b))

c = a

print(a is c) # true


