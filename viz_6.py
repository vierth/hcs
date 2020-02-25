# ploting a single list of data is not always super useful
# let's plot two values against each other
import matplotlib.pyplot as plt

# create some data
my_x = [i for i in range(20,30)]
my_y = [i for i in range(10, 0, -1)]
print(my_y)
my_y[4] = 12
print(my_y)
# plot the data
plt.scatter(my_x, my_y)

# give the plot a title
plt.title("Scatter plot")

# give the plot an x axis label
plt.xlabel("x values")
# y labels
plt.ylabel("y values")

plt.show()