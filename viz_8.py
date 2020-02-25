# ploting a single list of data is not always super useful
# let's plot two values against each other
import matplotlib.pyplot as plt

# create some data
my_x = [i for i in range(20,30)]
my_y = [i for i in range(10, 0, -1)]

my_y[4] = 12

# point colors
colors = ['blue', 'magenta', 'black', 'magenta', 'black', 'blue', '#ff00ff', '#115740', '0.8', 'green']

# give different sizes
sizes = [100, 50, 80, 100, 150, 20, 100, 90, 120, 60]

# plot the data
plt.scatter(my_x, my_y, s =sizes, c= colors)

# give the plot a title
plt.title("Scatter plot")

# give the plot an x axis label
plt.xlabel("x values")
# y labels
plt.ylabel("y values")

plt.show()