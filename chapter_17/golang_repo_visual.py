from git_api_repos import RepoAPI
import plotly.express as px


url = "https://api.github.com/search/repositories"
url += "?q=language:go+sort:stars+stars:>10000"

new_api_call = RepoAPI(url)

repo_links, stars, hover_texts = zip(*
            [(links, star_count, text) for 
            links, star_count, text in
            [((f"<a href='{repo_dict['html_url']}'>{repo_dict['name']}</a>"), 
            repo_dict['stargazers_count'],
            f"{repo_dict['owner']['login']} <br /> {repo_dict['description']}")
            for repo_dict in new_api_call.repo_dicts]]
            )


# for repo_dict in new_api_call.repo_dicts:

#     owner = repo_dict['owner']['login']
#     description = repo_dict['description']
#     hover_text = f"{owner} <br /> {description}"

#     hover_texts.append(hover_text)

# Make visualization
title = "Most-Starred Go Projects on Github"
labels = {'x': 'Repository', 'y': 'Stars'}

fig = px.bar(x=repo_links, y=stars, title=title, labels=labels,
             hover_name=hover_texts)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
                  yaxis_title_font_size=20)

fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)

fig.show()
