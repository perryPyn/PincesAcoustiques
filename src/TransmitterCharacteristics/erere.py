import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Données
y_data = np.array([.1, .5, .9, 1.05, 1.1, 1.7, 2.55, 3.6, 4.5, 4.8, 4.4, 3.4, 2.1, 1.0, .9, .8, .5, .2, .1])
x_data = np.linspace(-np.pi/2, np.pi/2, len(y_data))  # 19 points régulièrement espacés entre -pi/2 et pi/2

# Double gaussienne
def double_gaussian(x, A1, mu1, sigma1, A2, mu2, sigma2):
    return A1 * np.exp(-((x - mu1)**2) / (2 * sigma1**2)) + A2 * np.exp(-((x - mu2)**2) / (2 * sigma2**2))

# Estimation initiale
initial_guess = [4.5, 0, 0.6, 1.0, -1.0, 0.5]

# Ajustement
params, _ = curve_fit(double_gaussian, x_data, y_data, p0=initial_guess)
print(params)

# Générer la courbe ajustée
x_fit = np.linspace(-np.pi/2, np.pi/2, 300)
y_fit = double_gaussian(x_fit, *params)

# Affichage polaire
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

# Tracer les points de données
ax.plot(x_data, 20*np.log(y_data/max(y_data)), 'o', label='Données')

# Tracer la courbe ajustée
ax.plot(x_fit, 20*np.log(y_fit/max(y_fit)), label='Double gaussienne')

# Légende et affichage
ax.legend(loc='upper right')
plt.title("Double gaussienne en coordonnées polaires")
plt.show()