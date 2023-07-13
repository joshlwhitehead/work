import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

 

# Convert peak wavelength to standard deviation
peak_wavelength = 445
fwhm = 30
sigma = fwhm / (2 * np.sqrt(2 * np.log(2)))

 

# Generate x-axis values
x = np.linspace(400, 500, 1000)  # Wavelength range from 400nm to 500nm

 

# Generate normal distribution values
y = norm.pdf(x, peak_wavelength, sigma)

 

# Plot the normal distribution
plt.plot(x, y)
plt.xlabel('Wavelength (nm)')
plt.ylabel('Probability Density')
plt.title('Normal Distribution with Peak at 445nm and FWHM of 30')
plt.show()