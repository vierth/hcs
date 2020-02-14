# ngram tokenization function
def n_toke(text, n=1):
    tokens = []
    for i in range(len(text) - n + 1):
        token = text[i:i+n]
        tokens.append(token)
    return tokens

print(n_toke("testing", 2))