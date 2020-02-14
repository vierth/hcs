# we need to load the necessary libraries
import nltk, jieba

# open a file to do some analysis on and demo some of nltk's features
with open("sherlock.txt", 'r', encoding="utf8") as rf:
    text = rf.read()

# break into words and sentences
words_and_sentences = []
for sentence in nltk.sent_tokenize(text):
    words_and_sentences.append(nltk.word_tokenize(sentence))
    
words_and_sentences = [nltk.word_tokenize(sent) for sent in nltk.sent_tokenize(text)]

list_of_numbers = [i for i in range(100)]

print(list_of_numbers)

