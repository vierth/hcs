# we need to load the necessary libraries
import nltk, jieba

# open a file to do some analysis on and demo some of nltk's features
with open("sherlock.txt", 'r', encoding="utf8") as rf:
    text = rf.read()

# create words list
words = nltk.word_tokenize(text)

# filter words list
words = [word.lower() for word in words if word.isalnum()]

# create Texty object
my_text = nltk.Text(words)

# make a concordance
#my_text.concordance("holmes", 150, 100)

#my_text.similar("apartment")

# let's make a lexical dispersion plot
#my_text.dispersion_plot(["he said", "watson", "lestrade"])

#print(my_text.collocation_list())

freq = nltk.FreqDist(my_text)

#print(freq['and'])
#print(freq.most_common(10))
print(freq.hapaxes())