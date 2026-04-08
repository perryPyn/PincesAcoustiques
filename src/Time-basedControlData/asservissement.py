import numpy as np
import matplotlib.pyplot as plt

a = 0.010000828571428571 # mm/°

f_2224 = np.loadtxt('data/2224.txt')
f_2225 = np.loadtxt('data/2225.txt')
f_2226 = np.loadtxt('data/2226.txt')
f_2227 = np.loadtxt('data/2227.txt')
f_2228 = np.loadtxt('data/2228.txt')
f_2229 = np.loadtxt('data/2229.txt')
f_2230 = np.loadtxt('data/2230.txt')
f_2231 = np.loadtxt('data/2231.txt')


tau_2224,tau_2225,tau_2226,tau_2227,tau_2228,tau_2229,tau_2230,tau_2231 = 1000,500,250,150,130,110,120,125

t_2224 = f_2224[:,0]-5.0 # Offset temporel
x_2224 = f_2224[:,1]*10**3
y_2224 = f_2224[:,2]*10**3

t_2225 = f_2225[:,0]-4.4
x_2225 = f_2225[:,1]*10**3
y_2225 = f_2225[:,2]*10**3

t_2226 = f_2226[:,0]-1.6
x_2226 = f_2226[:,1]*10**3
y_2226 = f_2226[:,2]*10**3

t_2227 = f_2227[:,0]-3.7
x_2227 = f_2227[:,1]*10**3
y_2227 = f_2227[:,2]*10**3-0.001106 # Offset spatial

t_2228 = f_2228[:,0]-3.5
x_2228 = f_2228[:,1]*10**3
y_2228 = f_2228[:,2]*10**3

t_2229 = f_2229[:,0]-4.5
x_2229 = f_2229[:,1]*10**3
y_2229 = f_2229[:,2]*10**3+0.0001

t_2230 = f_2230[:,0]-3.09
x_2230 = f_2230[:,1]*10**3
y_2230 = f_2230[:,2]*10**3

t_2231 = f_2231[:,0]-3.85
x_2231 = f_2231[:,1]*10**3
y_2231 = f_2231[:,2]*10**3+0.000213


t = np.linspace(0,60,6000)
t_ms = t*1000 # Convertion en ms car millis() utilisé dans arduino l'est aussi
s_2224 = -180*np.sin(t_ms/tau_2224)*(1-np.exp(-t_ms/4000)) * a
s_2225 = -180*np.sin(t_ms/tau_2225)*(1-np.exp(-t_ms/4000)) * a
s_2226 = -180*np.sin(t_ms/tau_2226)*(1-np.exp(-t_ms/4000)) * a
s_2227 = -180*np.sin(t_ms/tau_2227)*(1-np.exp(-t_ms/4000)) * a
s_2228 = -180*np.sin(t_ms/tau_2228)*(1-np.exp(-t_ms/4000)) * a
s_2229 = -180*np.sin(t_ms/tau_2229)*(1-np.exp(-t_ms/4000)) * a
s_2230 = -180*np.sin(t_ms/tau_2230)*(1-np.exp(-t_ms/4000)) * a
s_2231 = -180*np.sin(t_ms/tau_2231)*(1-np.exp(-t_ms/4000)) * a


"""
plt.plot(t_2224,y_2224,'+',label='2224',color='darkolivegreen')
plt.plot(t,s_2224,'--',label='2224',color='olivedrab')
plt.plot(t_2225,y_2225,'+',label='2225',color='palevioletred')
plt.plot(t,s_2225,'--',label='2225',color='pink')
plt.plot(t_2226,y_2226,'+',label='2226',color='brown')
plt.plot(t,s_2226,'--',label='2226',color='indianred')
plt.plot(t_2227,y_2227,'+',label='2227',color='purple')
plt.plot(t,s_2227,'--',label='2227',color='purple')
plt.plot(t,s_2228,'--',label='2228',color='orange',linewidth=5)
plt.plot(t_2228,y_2228,'+',label='2228',color='blue')
plt.plot(t_2229,y_2229,'+',label='2229',color='darkorange')
plt.plot(t,s_2229,'--',label='2229',color='orange')
plt.plot(t,s_2230,'-',label='2230',color='lightgreen',linewidth=5)
plt.plot(t_2230,y_2230,'+',label='2230',color='darkgreen')
"""
plt.plot(t,s_2231,'--',label='2231',color='orange',linewidth=5)
plt.plot(t_2231,y_2231,'+',label='2231',color='blue')
"""
"""
plt.xlim(0,18)
#plt.ylim(-3,3)
#plt.legend()
plt.show()

epsilon = []
for i in range(len(t_2231)):
    epsilon.append(np.abs((-180*np.sin(t_2231[i]/tau_2231)*(1-np.exp(-t_2231[i]/4000)) * a)-y_2231[i]))
print(np.average(epsilon),max(epsilon))