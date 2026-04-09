import matplotlib.pyplot as plt
import numpy as np

angle    = np.arange(-90,91,10)*np.pi/180 # rad
tension1 = np.array([.01, .01, .2, 0.3,  0.5, 1.3, 1.7,  2.9, 3.5, 4.1, 3.7, 2.8, 1.7, 1.1,  .7, .4, .1,.1,.1]) # V
tension2 = np.array([.01, .2,  .5, 0.6,  2.4, 3.0, 5.0,  5.3, 5.2, 5.2, 5.3, 5.3, 4.9, 3.2, 2.3, .6, .3,.1,.1]) # V
tension3 = np.array([.1,  .5,  .9, 1.05, 1.1, 1.7, 2.55, 3.6, 4.5, 4.8, 4.4, 3.4, 2.1, 1.0,  .9, .8, .5,.2,.1]) # V

tension1 = 20*np.log(tension1/max(tension1))
tension2 = 20*np.log(tension2/max(tension2))
tension3 = 20*np.log(tension3/max(tension3))

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(angle, tension1, "+g", label="1",markersize=7)#Murata
ax.plot(angle, tension2, "+b", label="2",markersize=7)#Labo
ax.plot(angle, tension3, "+r", label="3",markersize=7)#Maquette 1
ax.set_theta_zero_location('N')
ax.set_thetamin(-90)
ax.set_thetamax(90)
ax.set_rlim(-86,10)
#ax.set_rticks([0,-10,-30,-50,-70])
#ax.set_rscale('log')
ax.grid(True)

def double_gaussian(x, a1, mu1, sigma1, a2, mu2, sigma2):
    return (a1 * np.exp(-0.5 * ((x - mu1) / sigma1) ** 2) +
            a2 * np.exp(-0.5 * ((x - mu2) / sigma2) ** 2))

def fitted_double_gauss(x):
    a1, mu1, sigma1 = 4.95, -0.386, 0.360
    a2, mu2, sigma2 = 4.83,  0.410, 0.342
    return (a1 * np.exp(-0.5 * ((x - mu1) / sigma1) ** 2) +
            a2 * np.exp(-0.5 * ((x - mu2) / sigma2) ** 2))

theta = np.linspace(0, 2 * np.pi, 500)
theta_wrapped = (theta + np.pi) % (2 * np.pi) - np.pi
r = fitted_double_gauss(theta_wrapped)
r = 20*np.log(r/max(r))
#ax.plot(theta, r, '-', label='Double Gaussienne', color='orange')


x_fit = np.linspace(-90, 90, 360)
x_fit_rad = x_fit * np.pi / 180  # pour le graphe polaire
popt = [1.43089287,0.51305302,16.04779486,2.62939996,-0.27855618,29.51715619]
y_fit = double_gaussian(x_fit, *popt)
y_fit = 20*np.log(y_fit/max(y_fit))
#ax.plot(x_fit_rad, y_fit, '-', label='Ajustement Double Gaussienne', color='orange')


ax.legend()
#ax.set_title("Diagramme de rayonnement des transducteurs", va='bottom')
plt.show()