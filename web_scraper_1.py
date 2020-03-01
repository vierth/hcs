# this script will request a page and save it to the hard drive
# always be sure to check the robots.txt!!
import urllib.request


# here is a url that i am going to acces via python

url ="https://en.wikipedia.org/wiki/United_States_Attorney_for_the_Southern_District_of_New_York"

with urllib.request.urlopen(url) as request:
    contents = request.read()

html_string = contents.decode()

with open("wiki_attorneys.html", 'w', encoding='utf8') as wf:
    wf.write(html_string)