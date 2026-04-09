import matplotlib.pyplot as plt
import numpy as np
import matplotlib.lines as lines


fig, ax = plt.subplots()

data = np.loadtxt('Labo.txt') # Maquette 1
f1 = data[:,0]*10**3#np.arange(30000,50000,500)#
s1 = data[:,1]
#s1 = [0.022,0.043,0.045,0.040,0.069,0.080,0.133,0.040,0.052,0.028,0.032,0.052,0.078,0.128,0.235,0.534,1.386,2.834,4.226,7.115,10.70,7.536,6.080,5.652,6.337,3.000,1.884,1.867,0.944,0.832,0.866,0.518,0.339,0.178,0.136,0.110,0.048,0.009,0.008,0.007] #data[:,1]
gain1 = 20*np.log(s1)
ax.plot(f1,gain1,'+r',label='Labo',linewidth=2)
#for i in range(len(f1)):
#    ax.add_line(lines.Line2D([f1[i],f1[i]], [gain1[i]-2,gain1[i]+2],lw=2, color='red', axes=ax))


f = np.linspace(30000,50000,10000)
w=2*np.pi*f
w_0 = 255500
Q = 19
H_0 = 1.8
"""
w_0 = 255600
Q = 18
H_0 = 2
"""


x=w/w_0
H = H_0**2 * x**4/(1+1.j*Q*(x-1/x))
G = H_0**2 * x**4/np.sqrt((1-(Q*(x-1/x))**2)**2+(Q*(x-1/x)**2))
ax.plot(f,20*np.log(G),linewidth=2)


ax.annotate('Q = '+str(Q),xy=(1, 0), xycoords='axes fraction',xytext=(-20, 41), textcoords='offset pixels',horizontalalignment='right',verticalalignment='bottom')
ax.annotate('w_0 = '+str(w_0),xy=(1, 0), xycoords='axes fraction',xytext=(-20, 62), textcoords='offset pixels',horizontalalignment='right',verticalalignment='bottom')

plt.xscale('log')
#plt.xlim(240000,270000)
plt.ylim(-100,60)
plt.legend(loc='upper left')
plt.grid()
plt.show()