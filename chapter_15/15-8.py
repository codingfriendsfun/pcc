import plotly.express as px

from die import Die


# Create 2D6
die_1 = Die()
die_2 = Die()

# Roll die; store results in list
results = []
for roll_num in range(1_000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

# Analyze results
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
poss_results = range(1, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize results
title = "Multiplying Results of Rolling 2D6"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Customize axis
fig.update_layout(xaxis_dtick=1)

fig.write_html('15-8 Chart.html')