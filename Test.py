import matplotlib.pyplot as plt
import numpy as np

# Create a figure and axis
fig, ax = plt.subplots()

# Set the x and y limits
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)

# Plot a line for each degree in 360 degrees
for angle in range(360):
    radians = np.radians(angle)
    x = np.cos(radians)
    y = np.sin(radians)
    ax.plot([0, x], [0, y], '-', color='gray', alpha=0.5)

# Show the plot
plt.show()