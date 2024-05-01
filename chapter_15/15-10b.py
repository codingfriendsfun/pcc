import plotly.express as px

from random_walk import RandomWalk

# Create and fill the walk
walk = RandomWalk()
walk.fill_walk()

# Graph the walk
title = "Random Walk"
x = walk.x_values
y = walk.y_values
fig = px.scatter(x=x, y=y, title=title, color_continuous_scale="YlOrBr")

fig.write_html('random_walk.html')
