from hn_article import HackerNewsAPI
import plotly.express as px


url = "https://hacker-news.firebaseio.com/v0/topstories.json"

new_api_call = HackerNewsAPI(url)
new_api_call.process_api_call()

# Holy mother of list comprehnsions
articles, comments = zip(*
                        [(links, star_count) for 
                        links, star_count in 
                        [(f"<a href='{sub_dict['hn_link']}'>{sub_dict['title']}</a>", 
                        sub_dict['comments']) 
                        for sub_dict in new_api_call.submission_dicts]])


# Book Code
# articles, comments = [], []

# for sub_dict in new_api_call.submission_dicts:
#     sub_link = sub_dict['hn_link']
#     sub_title = sub_dict['title']
#     comment_count = sub_dict['comments']

#     article = f"<a href='{sub_link}'>{sub_title}</a>"

#     comments.append(comment_count)
#     articles.append(article)



# Make visualization
title = "Most-Starred Go Projects on Github"
labels = {'x': 'Submission Title', 'y': 'Comments'}

fig = px.bar(x=articles, y=comments, title=title, labels=labels)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
                  yaxis_title_font_size=20)

fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)

fig.show()
