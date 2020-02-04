# Lists are containers for data held in a specific order

# you create an empty list with square brackets
my_list = []

# you can also use the list function
another_list = list()

# you can create a non-empty list with values seperated by commas:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Python will remember the order of the objects
another_list = [40, 2, -3, 18, 93]

# Lists can contain any type of python object
third_list = ["My", "name", "is", "Paul", "Vierthaler"]

# Lists can contain mixed data types (but you should avoid this)
number_four = [10.3, 15, "hello"]

# Lists of lists!
l_of_l = [[1,2], [4, 20], [14,-1]]

# List indexing is similar to string indexing
my_list[0] # first item
my_list[-1] # last item
my_list[2:5] # items 2 to 4
len(my_list) # gets the length

# adding to the list:
my_list.append(20) # changes the list in place, do not reassing to another variable

# adding at specific place
my_list.insert(2, 38) # insert 38 at index 2

# removing last item:
my_list.pop() # this will return whatever value it removes, so don't reassign 

# remove from specific index:
my_list.pop(2)


max(my_list) # get the max value
min(my_list) # get the minimum value



# sorting the list:
my_list.sort()
my_list.sort(reverse=True) # sort in reverse