import matplotlib.pyplot as plt
import numpy as np
import matplotlib.lines as lines


fig, ax = plt.subplots()

data1 = np.loadtxt('Bode1.txt') # Maquette 1
f1 = data1[:,0]*10**3  * 2*np.pi
s1 = data1[:,1]
gain1 = 20*np.log(s1)-151
ax.plot(f1,gain1,'+', color='darkred')
for i in range(len(f1)):
    ax.add_line(lines.Line2D([f1[i],f1[i]], [gain1[i]-1,gain1[i]+1],lw=2, color='darkred', axes=ax))
"""
data2 = np.loadtxt('Bode2.txt') # Maquette 1
f2 = data2[:,0]*10**3  * 2*np.pi
s2 = data2[:,1]
gain2 = 20*np.log(s2)-154
ax.plot(f2,gain2,'+', color='darkblue')
for i in range(len(f2)):
    ax.add_line(lines.Line2D([f2[i],f2[i]], [gain2[i]-1,gain2[i]+1],lw=2, color='darkblue', axes=ax))

data3 = np.loadtxt('Bode3.txt') # Maquette 1
f3 = data3[:,0]*10**3  * 2*np.pi
s3 = data3[:,1]
gain3 = 20*np.log(s3)-151.1
ax.plot(f3,gain3,'+', color='darkgreen')
for i in range(len(f3)):
    ax.add_line(lines.Line2D([f3[i],f3[i]], [gain3[i]-1,gain3[i]+1],lw=2, color='darkgreen', axes=ax))
"""
"""
Maquette 1 :
-151
"""
Q1 = 35
w_01 = 254180
"""
Labo :
-154
Q2 = 25
w_02 = 253290
"""
"""
Murata :
-151.1
Q3 = 36
w_03 = 255872
"""

w = np.linspace(100000,600000,100000)
ax.plot(w,-40*np.log(w)+450)
G1 = 20*np.log(1/np.sqrt(1+(Q1*(w/w_01-w_01/w))**2))
ax.plot(w,G1,'--r',label='Maquette 1')
G_max1 = max(G1)

dw = w_01/Q1
ax.axvline(x=w_01-dw/2, color="grey", linestyle="--")
ax.axvline(x=w_01+dw/2, color="grey", linestyle="--")

"""
G2 = 20*np.log(1/np.sqrt(1+(Q2*(w/w_02-w_02/w))**2))
ax.plot(w,G2,'--b',label='Labo')
G_max2 = max(G2)
G3 = 20*np.log(1/np.sqrt(1+(Q3*(w/w_03-w_03/w))**2))
ax.plot(w,G3,'--g',label='Murata')
G_max3 = max(G3)
#ax.axhline(y=G_max-3, color="gray", linestyle="--")
"""

def dicho(a,b,x=G_max1-3):
    w_m = (b+a)/2
    m = 20*np.log(1/np.sqrt(1+(Q1*(w_m/w_01-w_01/w_m))**2))
    while np.abs(m - x) > 1:
        w_m = (b-a)/2
        m = 20*np.log(1/np.sqrt(1+(Q1*(w_m/w_01-w_01/w_m))**2))
        print(w_m,m,x)
        if m>x: b=w_m
        else :  a=w_m
    return w_m

"""
w_cm = dicho(251950,252150)
w_cM = dicho(256200,256450)
w_cm = dicho(250000,250500)
w_cM = dicho(256000,256350)
w_cm = dicho(253650,253850)
w_cM = dicho(257900,258100)

ax.axvline(x=w_cm, color="grey", linestyle="--")
ax.axvline(x=w_cM, color="grey", linestyle="--")
ax.axvspan(w_cm, w_cM, color='yellow', alpha=0.3)

ax.annotate('dw = '+str(w_cM-w_cm),
            xy=(1, 0), xycoords='axes fraction',
            xytext=(-20, 20), textcoords='offset pixels',
            horizontalalignment='right',
            verticalalignment='bottom')
ax.annotate('Q = '+str(Q),
            xy=(1, 0), xycoords='axes fraction',
            xytext=(-20, 41), textcoords='offset pixels',
            horizontalalignment='right',
            verticalalignment='bottom')
ax.annotate('w_0 = '+str(w_0),
            xy=(1, 0), xycoords='axes fraction',
            xytext=(-20, 62), textcoords='offset pixels',
            horizontalalignment='right',
            verticalalignment='bottom')
print('dw = ',w_cM-w_cm)
"""

plt.xscale('log')
#plt.xlim(240000,270000)
#plt.ylim(-40,5)
plt.legend(loc='upper left')
plt.grid()
plt.show()