import matplotlib.pyplot as plt
import numpy as np

from die import Die


# Create die
die = Die()

# Roll die
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyze results
frequencies = []
poss_results = range(1, die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Graph data
plt.style.use('dark_background')
fig = plt.figure()

plt.bar(x=poss_results, height=frequencies)
plt.xlabel("Results")
plt.ylabel("Frequency of Results")
plt.title("Results of Rolling a D6 1k Times")

plt.show()
