import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import spectrogram

# Assuming you have a signal 'signal' sampled at 'fs' samples per second
# Here's some example signal data
fs = 1000  # Sample rate, Hz
t = np.linspace(0, 12, 12000)
signal = np.sin(2*np.pi*30*t) + np.sin(2*np.pi*60*t)

# Calculate the spectrogram
frequencies, times, Sxx = spectrogram(signal, fs)

# Plot the spectrogram
plt.figure()
plt.pcolormesh(times, frequencies, 10 * np.log10(Sxx), shading='gouraud')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()

# If you want to plot in 3D (like the image you've uploaded)
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a meshgrid for the frequency and time axes
T, F = np.meshgrid(times, frequencies)

# Plot the surface
surf = ax.plot_surface(T, F, 10 * np.log10(Sxx), cmap='viridis', linewidth=0, antialiased=False)

ax.set_ylabel('Frequency [Hz]')
ax.set_xlabel('Time [sec]')
ax.set_zlabel('Amplitude')

plt.show()
