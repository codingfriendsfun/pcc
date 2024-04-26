import matplotlib.pyplot as plt

#x_values = [1, 2, 3, 4, 5]
x_values = range(1, 5000)
y_values = [x**3 for x in x_values]

plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.BuGn, s=10)

# Set chart title; label axes
ax.set_title("Cubes", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(labelsize=14)

# Set range for each axis
ax.axis([0, 5100, 0, 130_000_000_000])

plt.show()