import os

# import some libraries from the scikit learn library.

# components we will need for our analysis
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances

from scipy.cluster.hierarchy import linkage, dendrogram

# the components for visualizing the results
import matplotlib.pyplot as plt

