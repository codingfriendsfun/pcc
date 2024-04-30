import plotly.express as px

from die import Die


# Create 2D8
die_1 = Die(8)
die_2 = Die(8)

# Roll die; store results in list
results = []
# My computer's fan briefly kicked in at 10M, but my patience hit its max lol
for roll_num in range(10_000_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize results
title = "Results of Rolling 2D8 10M Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Customize axis
fig.update_layout(xaxis_dtick=1)

fig.write_html('15-6 Chart.html')