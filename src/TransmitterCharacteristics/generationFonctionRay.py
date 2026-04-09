import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Données
x_data = np.arange(-90, 91, 10) * np.pi / 180  # en radians
y_data = [.01, .2, .5, 0.6, 2.4, 3.0, 5.0, 5.3, 5.2, 5.2, 5.3, 5.3, 4.9, 3.2, 2.3, .6, .3, .1, .1]
x_deg = x_data * 180 / np.pi  # pour le fit en degrés

# Fonction double gaussienne
def fitted_double_gauss(x):
    a1, mu1, sigma1 = 4.95, -0.386, 0.360
    a2, mu2, sigma2 = 4.83,  0.410, 0.342
    return (a1 * np.exp(-0.5 * ((x - mu1) / sigma1) ** 2) +
            a2 * np.exp(-0.5 * ((x - mu2) / sigma2) ** 2))

theta = np.linspace(0, 2 * np.pi, 500)
theta_wrapped = (theta + np.pi) % (2 * np.pi) - np.pi
r = fitted_double_gauss(theta_wrapped)

# Graphique polaire
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, polar=True)
ax.plot(x_data, y_data, 'o', label='Données')
ax.plot(theta, r, '-', label='Ajustement Double Gaussienne', color='orange')
ax.set_theta_zero_location('N')
ax.set_thetamin(-90)
ax.set_thetamax(90)
ax.legend(loc='upper right')
plt.title("Ajustement Double Gaussienne dans un graphique polaire")
plt.show()