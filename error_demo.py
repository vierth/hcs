'''
Some of the types of errors that you might run into.
'''

# for i in range(20):
#     print(i)


# another syntax error
a = "hello"
b = "this is another string"
c = 5

# let's create another error
my_list = [1,2,3,4,5,6]

#my_list[200]

# similar error with dictionariers
my_dictionary = {"run": 1953, "gorgonzola": "Delicious"}

try:
    my_dictionary["cheddar"]
except KeyError:
    my_dictionary["cheddar"] = "also delicious"

    print(my_dictionary)