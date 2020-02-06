# you will need to install jieba. Do it from the anaconda prompt on windows
# or from the terminal on a mac

import jieba

s = "她是清華大學的學生"

# tokenize the string and create a list
tokens = list(jieba.cut(s))

print(tokens)