from operator import itemgetter

import requests
import plotly.express as px


# Make API call; check response
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:5]:
    # Make new API call for each submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build directory for each article
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)

# Process dictionaries for graphing
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                          reverse=True)
article_names, comments = [], []
for submission_dict in submission_dicts:
    article_title = submission_dict['title']
    article_link = submission_dict['hn_link']
    article_title_link = f"<a href='{article_link}'>{article_title}</a>"
    article_names.append(article_title_link)
    comments.append(submission_dict['comments'])

# Make visualization
title = "Top Discussions on Hacker News"
labels = {'x': 'Article', 'y': 'Comments'}
fig = px.bar(x=article_names, y=comments, title=title, labels=labels)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
                  yaxis_title_font_size=20)

fig.update_traces(marker_color='CadetBlue', marker_opacity=0.6)

fig.show()
