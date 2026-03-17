import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
def factorial(n):
    if n<0:
        exit()
    elif n==0:
        return 1
    else:
        return n*factorial(n-1)

def legendre(theta,l):
    if l==0:
        return 1
    elif l==1:
        return np.cos(theta)
    else:
        return ((2*l-1)*(np.cos(theta)*legendre(theta,l-1))-(legendre(theta,l-2)*(l-1)))/l

def assc_legendre(theta,l,m):
    if m==0:
        return legendre(theta,l)
    elif m>0:
        return (1/abs(np.sin(theta)))*(((l-m+1)*(l-m+2)*assc_legendre(theta,l+1,m-1))-((l+m-1)*(l+m)*assc_legendre(theta,l-1,m-1)))/(2*l+1)
    elif m<0:
        m=abs(m)
        return ((-1)**m)*factorial(l-m)*assc_legendre(theta,l,m)/factorial(l+m)


def Y(theta,phi,l,m):
    N=(2*l+1)*factorial(l-m)/(4*np.pi*factorial(l+m))
    return (N**0.5)*assc_legendre(theta,l,abs(m))*np.exp(1j*m*phi)


l=int(input("Enter the value of l: "))
m=int(input("Enter the value of m: "))

if abs(m)>abs(l):
    exit("The absolute value of m cannot exceed that of l")

theta=np.linspace(10**(-5),np.pi*1**(0.999999),100)
phi=np.linspace(0,2*np.pi,200)
theta,phi=np.meshgrid(theta,phi)

Y_lm=Y(theta,phi,l,m)
Z=np.real(Y_lm)
r=np.abs(Z)

x = r * np.sin(theta) * np.cos(phi)
y = r * np.sin(theta) * np.sin(phi)
z = r * np.cos(theta)

fig=plt.figure(figsize=(8,6))
ax=fig.add_subplot(111,projection='3d')
ax.plot_surface(x,y,z,facecolors=plt.cm.Blues(np.abs(Z)/np.max(np.abs(Z))),rstride=1,cstride=1,alpha=0.7,linewidth=0)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(f"Spherical Harmonic for l={l}, m={m}")
plt.show()