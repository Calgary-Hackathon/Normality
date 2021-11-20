import requests

url = "https://reddit3.p.rapidapi.com/subreddit"

querystring = {"url":"https://www.reddit.com/r/mentalhealth"}

headers = {
    'x-rapidapi-host': "reddit3.p.rapidapi.com",
    'x-rapidapi-key': "52bc76e0d4mshf5ab184d6f6db96p1aa977jsnbdeefd8a916a"
    }

r = requests.request("GET", url, headers=headers, params=querystring)



print(r.selftext_html)