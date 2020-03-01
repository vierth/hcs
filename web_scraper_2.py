import urllib.request, json

# we don't just have to access wikipedia via scraping, we can use the api
api_url = "https://en.wikipedia.org/w/api.php?action=opensearch&format=json&search="


# let's add a searchterm to look for to run the search
search_term = "pandas"

api_call = api_url + search_term

wiki_header = {'User-Agent': 'Paul'}

wiki_request = urllib.request.Request(api_call, headers=wiki_header)

with urllib.request.urlopen(wiki_request) as request:
    response_data = request.read().decode()

wiki_results = json.loads(response_data)
print(wiki_results)