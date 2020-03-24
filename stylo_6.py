'''
Here I am going to do a Principal Component Analysis of the Federalist Papers
'''

# import the libraries that I'll use
import re, nltk, os
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA

import matplotlib.pyplot as plt

# fix font issues
from matplotlib import rcParams, font_manager
cfont = font_manager.FontProperties(fname='/Library/Fonts/Songti.ttc')
rcParams["font.family"] = cfont.get_name()


# ignore these files
ignore_files = {'.DS_Store', 'LICENSE', 'README.md', '.txt'}

# empty lists to hold the texts, and the titles of the texts
texts = []
titles = []

# capture the author
genres = []

# go through the corpus folder and grab the info I need
for root, dirs, files in os.walk('demo_corpus'):
    for filename in files:
        # check if i should ignore
        if filename not in ignore_files:
            with open(os.path.join(root, filename), encoding='utf8') as rf:
                texts.append(rf.read().lower())
                titles.append(filename[:-4].lower())
                genres.append(filename[:-4].split("_")[2])

# create count vectorizer object
count_vectorizer = TfidfVectorizer(max_features=1000, 
            use_idf=False,
            analyzer='char',
            ngram_range=(1,1))

# fit and transform the corpus
count_matrix = count_vectorizer.fit_transform(texts)

# make the results a dense array
count_matrix = count_matrix.toarray()

# perofrm PCA on the count_matrix
pca = PCA(n_components=2)


# transform the matrix
my_pca = pca.fit_transform(count_matrix)

# to plot we need some extra information
unique_vals = ['史藏', '集藏', '诗藏']

# we also want intergers for each of these labels
number_for_vals = [0, 1, 2, 3]

# map the names to the numbers
val_to_num = dict(zip(unique_vals, number_for_vals))

# integer list represnting the authors of the texts
text_class = np.array([val_to_num[genre] for genre in genres])

# provide some colors for the graph
color_dict = {"史藏":"magenta", "集藏":"cyan", "诗藏":"green"}

# make a list of colors for matplotlib
colors = [color_dict[val] for val in unique_vals]

# create the plot
for color, class_number, value in zip(colors, number_for_vals, unique_vals):
    plt.scatter(my_pca[text_class==class_number, 0],
                my_pca[text_class==class_number, 1],
                label=value,
                c=color)

# add a legend
plt.legend()

# show the plot
plt.show()
















