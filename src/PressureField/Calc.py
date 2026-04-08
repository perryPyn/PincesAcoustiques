from numpy import array, sqrt, cos, sin, arcsin, exp, arctan, abs, pi, gradient,savez
from scipy.special import jv as J_0 # fonction de Bessel
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

print('Starting...')

w = 40_000 # Hz, Fréquence du travail des transudcteurs
T = 298 # K, Température du milieu de l'hôte
c_0 = sqrt(7/5 * (8.314*T)/(28.965*10**-3)) # m/s, vitesse dans le milieu de l'hôte
c_p = 392 # m/s, vitesse dans le milieu de la particule
rho_0 = 1.174 # kg/m**3, densité du milieu de l'hôte
rho_p = 44.9 # kg/m**3, densité du milieu de la particule
P_0 = 1 # W, Puissance définie par le transducteur
k = w/c_0 # Nombre d'onde
d_p = 3.2*10**-3 # m, diamètre de la particule
dEmetteur = 9.9*10**-3 # m, diamètre d'un transducteur
r = dEmetteur/2 # m, Rayon du piston de Farfield
V = 4/3*pi*(d_p**2)/4 # m**3, Volume de la particule

K1 = 1/4 * V * (1/(c_0**2 * rho_0) - 1/(c_p**2 * rho_p))
K2 = 3/4 * V * ((rho_0 - rho_p)/(w**2 * rho_0 * (rho_0 - 2*rho_p)))

phi = array([0,0,0,0,0,0,0,0]) # phase des 8 transducteurs
posEmetteurs = array([(3.4,3.7,-0.1),(13.8,4,-0.1),(14,14,-0.1),(3.4,14,-0.1),(3.4,3.7,20.01),(13.8,4,20.01),(14,14,20.01),(3.4,14,20.01)]) # (x,y,z), origine du repère en bas à gauche du tableau
#phi = array([0,0])
#posEmetteurs = array([(0,0,-0.1),(0,0,27.01)])

res = 50
h = 0.1

dx=dEmetteur*(len(posEmetteurs)+1)
dy=dEmetteur*(len(posEmetteurs)+1)
dz=27

def PosPoint(res=res,dx=dx,dy=dy,dz=dz):
	"""
		dTho = dx*dy*dz est le volume de travail définit par l'espace
		entre la surface des transducteurs
	"""
	dx/=res;dy/=res;dz/=res
	return array([[i*dx for i in range(res) for _ in range(res) for _ in range(res)],
				  [j*dy for _ in range(res) for j in range(res) for _ in range(res)],
				  [k*dz for _ in range(res) for _ in range(res) for k in range(res)]])


def PCmplx(d_i,theta_i,phi_i): # pression complexe en un point	
	mod_p = P_0 * J_0(0,k*r*sin(theta_i)) * (1/d_i)
	arg_p = k*d_i+phi_i
	#p = mod_p*exp(arg_p*1.j)
	return mod_p,arg_p


def dxPCmplx(x_i,z_i,phi_i,h=h):
	d_i = sqrt(x_i**2+z_i**2)
	theta_i = arctan(x_i/z_i)
	dJ_0x = (J_0(0,k*r*sin(arctan((x_i+h)/z_i))) - J_0(0,k*r*sin(arctan((x_i-h)/z_i))))/(2*h)
	
	return abs(P_0 * (J_0(0,k*r*sin(theta_i)) * x_i/d_i**2 * exp(1.j*(k*d_i+phi_i)) * (1.j*k - 1/d_i)
					  + k*r*cos(theta_i) * z_i/d_i**3 * exp(1.j*(k*d_i+phi_i)) * dJ_0x))


def dzPCmplx(x_i,z_i,phi_i,h=h):
	d_i = sqrt(x_i**2+z_i**2)
	theta_i = arctan(x_i/z_i)
	dJ_0z = (J_0(0,k*r*sin(arctan((x_i)/z_i+h))) - J_0(0,k*r*sin(arctan((x_i)/z_i-h))))/(2*h)
	
	return abs(P_0 * (J_0(0,k*r*sin(theta_i)) * z_i/d_i**2 * exp(1.j*(k*d_i+phi_i)) * (1.j*k - 1/d_i)
					  - k*r*cos(theta_i) * x_i/d_i**3 * exp(1.j*(k*d_i+phi_i)) * dJ_0z))
	
	
posPoints = PosPoint()

def ChampPCmplx(phi=phi,points=posPoints,emetteurs=posEmetteurs):
	mod_p = [0 for _ in range(len(points[0]))]

	for i in range(len(emetteurs)):
		for j in range(len(points[0])):
			d_i = sqrt((emetteurs[i][0]-points[0][j])**2+(emetteurs[i][1]-points[1][j])**2+(emetteurs[i][2]-points[2][j])**2)
			theta_i = arcsin(sqrt((emetteurs[i][0]-points[0][j])**2+(emetteurs[i][1]-points[1][j])**2)/d_i) # rad
			mod_p[j] += PCmplx(d_i,theta_i,phi[i])[0]
	
	return points,mod_p
	

def CalcU(phi=phi,points=posPoints,emetteurs=posEmetteurs):
	dpx = array([0 for _ in range(len(points[0]))])
	dpz = array([0 for _ in range(len(points[0]))])
	p   = array(ChampPCmplx(phi)[1])
		
	for i in range(len(emetteurs)):
		for j in range(len(points[0])):
			x_i = sqrt((emetteurs[i][0]-points[0][j])**2+(emetteurs[i][1]-points[1][j])**2)
			z_i = abs(emetteurs[i][2]-points[2][j])
			dpx[i] += dxPCmplx(x_i,z_i,phi[i])
			dpz[i] += dzPCmplx(x_i,z_i,phi[i])
	U = K1*p**2 - K2*(2*dpx**2 + dpz**2)
	
	return points,U,p
#print(CalcU(phi=[0,0],points=PosPt(res=2),emetteurs=[(1,0,0),(0,1,0)]))
	
def CalcF(phi=phi,points=posPoints,emetteurs=posEmetteurs):
	points,U,p = CalcU()
	
	U3d = [] # Conversion en matrice pour le gradient
	n = 0
	for i in range(res):
		U3d.append([])
		for _ in range(res):
			U3d[i].append(U[n*res:(n+1)*res])
			n+=1
	u,v,w = gradient(U3d,dx/res,dy/res,dz/res)

	U,V,W = [],[],[] # reconversion au format d'origine
	for i in range(res):
		for j in range(res):
			for k in range(res):
				U.append(-1*u[i][j][k])
				V.append(-1*v[i][j][k])
				W.append(-1*w[i][j][k])
	F = U,V,W

	return points,U,p,F

# Calculs
pt,U,p,F = CalcF()
savez('var',pt=pt,U=U,p=p,res=res,phi=phi,F=F)
print('Done!')
