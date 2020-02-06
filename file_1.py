# writes to file
# writefile = open("newfile.txt", 'w')
# writefile.write("a")
# writefile.close()

with open("newfile.txt", 'w') as writefile:
    writefile.write("This is slightly more interesting")

with open("newfile.txt", 'r', encoding="utf8", errors='replace') as readfile:
        contents = readfile.read()
        print(contents)

with open("newfile.txt", 'a') as writefile:
    for i in range(10000):
        writefile.write("yahoooo")



