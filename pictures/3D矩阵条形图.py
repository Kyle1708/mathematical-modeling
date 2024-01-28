import numpy as np
import matplotlib.pyplot as plt

# Generate random data for the matrix
data = np.random.rand(10, 10)

# Create a figure and axis for the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create x, y coordinates for the bars
xpos, ypos = np.meshgrid(range(10), range(10))

# Flatten the data and convert it to a 1D array
zpos = np.zeros_like(xpos)
dx = dy = 0.8
dz = data.flatten()

# Generate random colors for each bar
colors = np.random.rand(len(dz))
colors = plt.cm.viridis(colors)  # Convert colors to valid RGBA format

# Plot the bars
ax.bar3d(xpos.flatten(), ypos.flatten(), zpos.flatten(), dx, dy, dz, color=colors)

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Matrix Bar Chart')

# Show the plot
plt.show()

# Plot the bars
ax.bar3d(xpos.flatten(), ypos.flatten(), zpos.flatten(), dx, dy, dz, color=colors)

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Matrix Bar Chart')

# Show the plot
plt.show()
