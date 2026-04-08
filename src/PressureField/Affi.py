from numpy import load,abs
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

c = 2

# Variables
tempVar = load('var.npz')
x,y,z = tempVar['pt']
U = tempVar['U']
p = tempVar['p']
res = tempVar['res']
phi = tempVar['phi']
u,v,w = tempVar['F']

# Graphes
fig = plt.figure()
ax = plt.axes(projection='3d')	

#ax.scatter3D(x, y, z, c=p, cmap='Greens', vmin=0, vmax=90, s=(-0.22*res+24))
#ax.scatter3D(x, y, z, c=U, cmap='Grays',s=(-0.22*res+24))

if   c == 0: # Afficher le module de la pression
	x_min_p = []; y_min_p = []; z_min_p = []; p_min = []
	for j in range(len(x)):
		if 	p[j] > .5:
			x_min_p.append(x[j])
			y_min_p.append(y[j])
			z_min_p.append(z[j])
			p_min.append(p[j])
	ax.scatter3D(x_min_p, y_min_p, z_min_p, c=p_min, cmap='Greens', vmin=0, vmax=10, s=(-0.22*res+24))
elif c == 1 : # Afficher le potentiel de Gorkov
	x_min_U = []; y_min_U = []; z_min_U = []; U_min = []
	for j in range(len(x)):
		if abs(U[j]) > 8:
			x_min_U.append(x[j])
			y_min_U.append(y[j])
			z_min_U.append(z[j])
			U_min.append(U[j])
	ax.scatter3D(x_min_U, y_min_U, z_min_U, c=U_min, cmap='Blues',s=(-0.22*res+24))
elif c == 2 : # Afficher la force acoustique
	x_min_F = []; y_min_F = []; z_min_F = []; u_min_F = []; v_min_F = []; w_min_F = []
	for j in range(len(x)):
		if (u[j]-x[j])**2+(v[j]-y[j])**2+(w[j]-z[j])**2 > 26**2:
			x_min_F.append(x[j])
			y_min_F.append(y[j])
			z_min_F.append(z[j])
			u_min_F.append(u[j])
			v_min_F.append(v[j])
			w_min_F.append(w[j])
	ax.quiver(x_min_F, y_min_F, z_min_F, u_min_F, v_min_F, w_min_F, color='red', length = .003, normalize=True)

plt.show()
