import numpy as np
import matplotlib.pyplot as plt

def fitted_double_gauss(x):
    A1, mu1, sigma1 = 4.95, -0.386, 0.360
    A2, mu2, sigma2 = 4.83,  0.410, 0.342
    g1 = A1 * np.exp(-0.5 * ((x - mu1) / sigma1)**2)
    g2 = A2 * np.exp(-0.5 * ((x - mu2) / sigma2)**2)
    return g1 + g2


fig, ax = plt.subplots()
# Données d'origine
x_data = np.arange(-90, 91, 10)*np.pi/180
y_data = [.01, .2, .5, 0.6, 2.4, 3.0, 5.0, 5.3, 5.2, 5.2, 5.3, 5.3, 4.9, 3.2, 2.3, .6, .3, .1, .1]

# Évaluation
x_vals = np.linspace(-90, 91, 500)*np.pi/180
y_vals = fitted_double_gauss(x_vals)

# Affichage
ax.plot(x_data, y_data, 'o', label='Données')
ax.plot(x_vals, y_vals, '-', label='Approximation')
ax.legend()
ax.grid(True)
plt.show()
