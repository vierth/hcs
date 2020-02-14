# we need to load the necessary libraries
import nltk, jieba

# open a file to do some analysis on and demo some of nltk's features
with open("sherlock.txt", 'r', encoding="utf8") as rf:
    text = rf.read()

# tokenize into sentences
sentences = nltk.sent_tokenize(text)

# let's tokenize into words
words = nltk.word_tokenize(text)

# tokenize a chinese sentence
chinese_sentence = "日文章魚怎麼說"
c_words = jieba.cut(chinese_sentence)

for word in c_words:
    print(word)