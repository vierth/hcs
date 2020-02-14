# we need to load the necessary libraries
import nltk, jieba

# make a function to find lexical diversity
def lex(words):
    return len(set(words))/len(words)

# open a file to do some analysis on and demo some of nltk's features
with open("sherlock.txt", 'r', encoding="utf8") as rf:
    text = rf.read() 

# create words list
words = nltk.word_tokenize(text)

# filter words list
words = [word.lower() for word in words if word.isalnum()]

words_one = words[1000:11000]

words_two = words[45000:55000]

print(lex(words_one))
print(lex(words_two))
# number of words in the document
# num_words = len(words)

# unique_words = set(words)

# num_unique_words = len(unique_words)

# print(num_unique_words/num_words)