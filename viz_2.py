# let's import the matplotlib library
#import matplotlib.pyplot as plt

from matplotlib import pyplot as plt

# https://matplotlib.org/users/pyplot_tutorial.html

# Plotting a line is very easy.
# create some data
my_data = [i*2 for i in range(10)]

# create some data for a second line
my_data_2 = [i/2 for i in range(10)]


# create a plot
plt.plot(my_data)
# add a second line
plt.plot(my_data_2)

# show the plot
plt.show()