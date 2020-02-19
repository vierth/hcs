# we can match one pattern or another with a pipe
import re

results = re.findall("cat|dog", "Is this a cat or a dog?")
print(results)