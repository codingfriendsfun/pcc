import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 8, 27, 64, 125]

plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)

# Set chart title; label axes
ax.set_title("Cubes", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value, fontsize=14")

# Set size of tick labels
ax.tick_params(labelsize=14)

# Set range for each axis
ax.axis([0, 6, 0, 150])

plt.show()