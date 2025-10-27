import requests
import plotly.express as px

url = "https://api.github.com/search/repositories"

url += '?q=language:python+sort:stars+stars:>10000'


# Make an API call and check the response
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Convert response object to a dictionary

response_dict = r.json()

print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")

repo_dicts = response_dict['items']

repo_links, stars, hover_texts = [], [], []
for repo_dict in repo_dicts:
    stars.append(repo_dict['stargazers_count'])

    # Making Links
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    # Making Tooltips
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)
# Make visualization
title = "Most-Starred Python Projects on Github"
labels = {'x': 'Repository', 'y': 'Stars'}
fig = px.bar(x=repo_links, y=stars, color=stars, title=title,
             labels=labels, hover_name=hover_texts, color_continuous_scale='Viridis',)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
                  yaxis_title_font_size=20)
fig.update_traces(marker_opacity=0.6)
fig.write_html('repos_bar_chart.html')
