import plotly.express as px

from die import Die


# Create a D6
die = Die()

# Make some rolls; store results in list
results = [die.roll() for roll_num in range(1000)]

# Analyze results
frequencies = [results.count(value) for value in range(1, die.num_sides+1)]

# Visualize results
poss_results = range(1, die.num_sides+1)
title = "Results of Rolling a D6 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.write_html('dice_visual.html')
