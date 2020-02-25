import matplotlib.pyplot as plt

data = [1,2,3,4,5,6,7, 8]
data_2 = [4, 2, 6, 1, 1, 8, 9, 3]

# first thing I need to do is create a figure object
figure = plt.figure()

# add a subplot (here, i'll be adding 2 subplots and specifying
# which one to plot in)
sub_plot_1 = figure.add_subplot(2, 1, 1)

sub_plot_1.plot(data, linestyle='--')
sub_plot_1.plot(data_2, drawstyle='steps')

# plot the same data but with swaped styles in second plot
sub_plot_2 = figure.add_subplot(2,1,2)
sub_plot_2.plot(data, drawstyle='steps')
sub_plot_2.plot(data_2, linestyle='--')

# set the subpplot titles
sub_plot_1.set_title("Numbers!")
sub_plot_2.set_title("More Numbers!")
sub_plot_2.set_xlabel("x")
sub_plot_1.set_xlabel("x")

sub_plot_1.set_xticks([0,3,7])

sub_plot_2.set_yticklabels([ 'f', 'g', 'h', 'i', 'j'], rotation = 15)

plt.tight_layout()
plt.show()