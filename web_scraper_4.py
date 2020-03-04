# if we want to efficiently parse html, we can use BeautifulSoup
from bs4 import BeautifulSoup

with open("wiki_attorneys.html", "r", encoding='utf8') as rf:
    html = rf.read()

soup = BeautifulSoup(html, 'lxml')

#print(soup.prettify())

# let's get all of the links
links = soup.find_all("a")

for link in links:
    url = link.get("href")
    link_text = link.get_text()
    #print(f"{link_text}: {url}")

#full_text = soup.find_all(text=True)

for item in soup(["script", "style"]):
    item.extract()

# all_text = soup.get_text()
# print(all_text)

lists = soup.find_all("ul")

print(lists[2].get_text())

atts_general = lists[2].find_all("li")

# for at in atts_general:
#     print(at.get_text())

# atts_general[-1].text