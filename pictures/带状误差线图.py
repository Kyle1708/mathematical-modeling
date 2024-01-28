import matplotlib.pyplot as plt
import numpy as np

# Generate some sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)
error = np.random.normal(0, 0.1, size=len(x))

# Plot the band plot with error bars
plt.plot(x, y, color='blue', label='Data')
plt.fill_between(x, y-error, y+error, color='lightblue', alpha=0.5, label='Error')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Band Plot with Error Bars')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
