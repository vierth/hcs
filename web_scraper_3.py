import urllib.request, json

# we don't just have to access wikipedia via scraping, we can use the api
api_url = "https://zh.wikisource.org/w/api.php?action="

# tell the qpi what action you want to take
action = 'query'

# different terms in the api are connect with ampersands
connector = '&'

# you can also set properties for your query
prop = 'linkshere'

# set the search method
search_method = 'titles'

# let's add a searchterm to look for to run the search
search_term = "四庫全書總目提要"

#escape the search term
search_term = urllib.parse.quote(search_term)

# if search_term has spaces, replace with underscroes
if " " in search_term:
    search_term = search_term.replace(" ", "_")

api_call = f'{api_url}{action}&prop={prop}&format=json&{search_method}={search_term}'

wiki_header = {'User-Agent': 'Paul'}

wiki_request = urllib.request.Request(api_call, headers=wiki_header)

with urllib.request.urlopen(wiki_request) as request:
    response_data = request.read().decode()

wiki_results = json.loads(response_data)
print(wiki_results)