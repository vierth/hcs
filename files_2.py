with open('jpm.txt', 'r', encoding='utf8') as rf:
    jpm=rf.read()

jpm = jpm[jpm.find("*** START OF THIS"):jpm.find("*** END OF")]

print(jpm[:1000])