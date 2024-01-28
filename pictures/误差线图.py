import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [1, 3, 2, 4, 5]
error = [0.5, 0.3, 0.2, 0.4, 0.1]

# Plotting the error line graph
plt.errorbar(x, y, yerr=error, fmt='o', capsize=4)

# Adding labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Error Line Graph')

# Displaying the graph
plt.show()
