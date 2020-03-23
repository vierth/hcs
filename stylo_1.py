import os

# import some libraries from the scikit learn library.

# components we will need for our analysis
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances

from scipy.cluster.hierarchy import linkage, dendrogram

# the components for visualizing the results
import matplotlib.pyplot as plt

# let's filter out texts we do NOT want to analyze
# for example, you roperating system might have hidden files that will screw up
# the calculations
ignore_files = {".DS_Store", "LICENSE", "README.md"}

# an empty list to store all of the texts in my corpus
texts = []

# keep track of the filenames for use later?
titles = []

# keep track of the author of each these
authors = []


# load in our texts

for root, dirs, files in os.walk("fedpapers"):
    for filename in files:
        if filename not in ignore_files:
            with open(os.path.join(root, filename)) as rf:
                texts.append(rf.read())
                titles.append(filename[:-4])
                authors.append(filename[:-4].split("_")[1])

# creating an object that will calculate our term frequencies
count_vectorizer = TfidfVectorizer(max_features=1000, use_idf=False)

# let's get those frequencies
count_matrix = count_vectorizer.fit_transform(texts)

# measure the distances between all points in this matrix
similarity = euclidean_distances(count_matrix)

# let's cluster documents together
linkages = linkage(similarity, "ward")

# let's make the dendrogram
dendrogram(linkages, labels=authors, orientation="right", 
            leaf_font_size=8, leaf_rotation=45)

plt.tick_params(axis='x', which='both', bottom=False, top=False, 
                labelbottom=False)

plt.tight_layout()

plt.show()


