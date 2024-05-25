import plotly.express as px

from die import Die

# Create a D6
die_1 = Die()
die_2 = Die()

results = []

for roll_num in range(50_000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

freqs = []
max_result = die_1.num_sides * die_2.num_sides
poss_results = range(2, max_result+1)

for value in poss_results:
    freq = results.count(value)
    freqs.append(freq)

# Visualize the results.
title = "Results of Rolling 2 D6 Die 50,000 Times with multiplication."
labels = {'x': 'Result', 'y': 'Frequency of Result',}

fig = px.bar(x=poss_results, y=freqs, title=title, labels=labels)

fig.update_layout(xaxis_dtick=1)

fig.show()
