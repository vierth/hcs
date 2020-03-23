# Very often it is useful to convey information using color. What if we wanted 
# to color code the leaf labels based on the year in which the story was
# written? This code will do that:
import re, nltk, os
from pandas import DataFrame
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt
from matplotlib import rcParams, font_manager

# set the font so it works in Chinese!
cfont = font_manager.FontProperties(fname='/Library/Fonts/Songti.ttc')

rcParams['font.family'] = cfont.get_name()

ignoreFiles = set([".DS_Store","LICENSE","README.md"])
texts = []
titles = []
# capture the author!
authors = []
for root, dirs, files in os.walk("demo_corpus"):
    for filename in files:
        if filename not in ignoreFiles:
            with open(os.path.join(root,filename)) as rf:
                texts.append(rf.read().lower())
                titles.append(filename[:-4].lower())
                authors.append(filename[:-4].split("_")[2])
                
print(set(authors))                

countVectorizer = TfidfVectorizer(max_features=1000, use_idf=False, token_pattern='(?u)\w',)
countMatrix = countVectorizer.fit_transform(texts)
similarity = euclidean_distances(countMatrix)
linkages = linkage(similarity,'ward')


#c_font = mfm.FontProperties(fname='/Library/Fonts/Songti.ttc')


dendrogram(linkages, labels=authors, orientation="right", leaf_font_size=8,leaf_rotation=45)
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.tight_layout()

ax = plt.gca()

labels = ax.get_ymajorticklabels()

#color_dict = {"Hamilton":"magenta", "Madison":"cyan", "Jay":"green", "Unknown":"black"}
color_dict = {'诗藏':"magenta", '集藏':"cyan", '史藏':"green"}


for label in labels:
    label_text = label.get_text()
    label.set_color(color_dict[label_text])

plt.show()
