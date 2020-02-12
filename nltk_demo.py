# Fun times doing things with nltk! Let's get started

# A good resource is https://www.nltk.org/book/

# to use nltk you have to first import it
import nltk

with open("sherlock.txt", 'r', encoding="utf8") as rf:
    text = rf.read()

text = text[text.find("*** START"): text.rfind("*** END")]

sentences = nltk.sent_tokenize(text)

words = nltk.word_tokenize(text)

sent_words = []

for sent in sentences:
    sent_words.append(nltk.word_tokenize(sent))

print(words[100])


words = [word for word in words if word != ""]