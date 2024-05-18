import matplotlib.pyplot as plt


x_values = list(range(5001))
y_values = [x**3 for x in x_values]

plt.style.use('seaborn-v0_8-pastel')

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)

# Set chart title and label axis
ax.set_title("Cube numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# Set the range for each axis.
ax.axis([0, 5100, 0, 5100**3])
ax.ticklabel_format(style='plain')


plt.show()
