import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


sns.set()

data = np.random.randint(20, size=15)

figure = plt.figure()

my_plot = figure.add_subplot(1,1,1)

# get an index for the data
index = [i for i in range(len(data))]

sns.barplot(index, data)

plt.show()