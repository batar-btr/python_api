import requests

url = "https://api.github.com/search/repositories"

url += '?q=language:python+sort:stars+stars:>10000'


# Make an API call and check the response
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Convert response object to a dictionary

response_dict = r.json()

# Results processing

print(response_dict.keys())
