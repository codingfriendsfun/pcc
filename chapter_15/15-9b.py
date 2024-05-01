import plotly.express as px

from die import Die


# Create 1D6, 1D10
die_1 = Die()
die_2 = Die(10)

# Make some rolls; store results in list
results = [die_1.roll() + die_2.roll() for roll_num in range(50_000)]

# Analyze results
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)

frequencies = [results.count(value) for value in poss_results]

# Visualize results
title = "Results of Rolling 1D6 and 1D10 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Customize axis
fig.update_layout(xaxis_dtick=1)

fig.write_html('dice_visual.html')