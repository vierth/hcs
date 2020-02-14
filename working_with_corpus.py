import os, nltk

# make a function to find lexical diversity
def lex(words):
    return len(set(words))/len(words)

# let's create a copule of objects to keep track of our data
texts = []
labels = []

# iterate through every file in the corpus folder
for root, dirs, files in os.walk("corpus"):
    # go through each file
    for file_name in files:
        # open the file
        with open(os.path.join(root, file_name),'r', encoding='utf8') as rf:
            text = rf.read()
            words = nltk.word_tokenize(text)
            words = [word.lower() for word in words if word.isalnum()]
            texts.append(words)
            labels.append(file_name[:-4])

for title, words in zip(labels, texts):
    lex_div = lex(words)
    print(f"{title} has a lexical diversity of {lex_div}, and is {len(words)} long.")
