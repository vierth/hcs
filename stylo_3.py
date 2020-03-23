import os

# import some libraries from the scikit learn library.

# components we will need for our analysis
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances

from scipy.cluster.hierarchy import linkage, dendrogram

# the components for visualizing the results
import matplotlib.pyplot as plt

# fix font issues
from matplotlib import rcParams, font_manager
cfont = font_manager.FontProperties(fname='/Library/Fonts/Songti.ttc')
rcParams["font.family"] = cfont.get_name()

# let's filter out texts we do NOT want to analyze
# for example, you roperating system might have hidden files that will screw up
# the calculations
ignore_files = {".DS_Store", "LICENSE", "README.md"}

# an empty list to store all of the texts in my corpus
texts = []

# keep track of the filenames for use later?
titles = []

# keep track of the author of each these
cat = []


# load in our texts

for root, dirs, files in os.walk("demo_corpus"):
    for filename in files:
        if filename not in ignore_files:
            with open(os.path.join(root, filename)) as rf:
                texts.append(rf.read())
                titles.append(filename[:-4])
                cat.append(filename[:-4].split("_")[2])

print(set(cat))


# creating an object that will calculate our term frequencies
count_vectorizer = TfidfVectorizer(max_features=1000, use_idf=False,
                                analyzer="char")
# (?u)\b\w\w+\b

# let's get those frequencies
count_matrix = count_vectorizer.fit_transform(texts)

# measure the distances between all points in this matrix
similarity = euclidean_distances(count_matrix)

# let's cluster documents together
linkages = linkage(similarity, "ward")

# let's make the dendrogram
dendrogram(linkages, labels=cat, orientation="right", 
            leaf_font_size=8, leaf_rotation=45)

plt.tick_params(axis='x', which='both', bottom=False, top=False, 
                labelbottom=False)

# create a dictionary with colors to make the plot more colorful
#color_dict = {'Jay':"green", 'Madison':"cyan", 'Hamilton':"magenta",
#             'Unknown':"black"}
color_dict = {'史藏':"green", '诗藏':"cyan", '集藏':"magenta"}
# This functions as a handle for visual elements inside the plot I am creating
ax = plt.gca()

# get the labels from the plot
labels = ax.get_ymajorticklabels()

# go through the labels and change the color
for label in labels:
    label.set_color(color_dict[label.get_text()])

plt.tight_layout()

plt.show()


