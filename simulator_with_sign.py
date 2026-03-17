import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math

a=1 

def legendre(x,l):
    if l==0:
        return 1
    elif l==1:
        return x
    else:
        return ((2*l-1)*(x*legendre(x,l-1))-(legendre(x,l-2)*(l-1)))/l

def assc_legendre(x,l,m):
    if m==0:
        return legendre(x,l)
    elif m>0:
        return (1/((1-x**2)**0.5))*(((l-m+1)*(l-m+2)*assc_legendre(x,l+1,m-1))-((l+m-1)*(l+m)*assc_legendre(x,l-1,m-1)))/(2*l+1)
    elif m<0:
        m=abs(m)
        return ((-1)**m)*math.factorial(l-m)*assc_legendre(x,l,m)/math.factorial(l+m)


def Y(theta,phi,l,m):
    N=(2*l+1)*math.factorial(l-m)/(4*np.pi*math.factorial(l+m))
    t=np.cos(theta)
    return (N**0.5)*assc_legendre(t,l,abs(m))*np.exp(1j*m*phi)

def laguerre(x,n):
    if n==0:
        return 1
    elif n==1:
        return 1-x
    elif n>=1:
        return (((2*n-x-1)*laguerre(x,n-1))-((n-1)*laguerre(x,n-2)))/n
    else:
        n=abs(n)
        return math.exp(x)*laguerre(-x,n-1)

def assc_laguerre(x,n,l):
    if n==0:
        return 1
    elif l==0:
        return laguerre(x,n)
    elif n==1:
        return 1+l-x
    elif n>=1:
        return (((2*n-1+l-x)*assc_laguerre(x,n-1,l))-((n-1+x)*assc_laguerre(x,n-2,l)))/n
    
def assc_laguerre_b(x,n,l):
    return assc_laguerre(x,n,l)*math.factorial(n)


def Ra(r,n,l):
    n1=(-(2/n/a)**1.5)*((2*r/n/a)**l)*(np.exp(-r/n/a))
    n2= math.factorial(n-l-1)*0.5/n/((math.factorial(n+l))**3)
    return n1*assc_laguerre_b(2*r/n/a,n+l,2*l+1)*(n2**0.5)


n=int(input("Enter the value of n: "))
l=int(input("Enter the value of l: "))
m=int(input("Enter the value of m: "))

if abs(m)>abs(l) and n<=l and n<=0:
    exit("Please enter the correct values for the quantum numbers")

n_r=103;n_theta=101;n_phi=97
theta=np.linspace(10**(-5),np.pi**(0.999999),n_theta)
phi=np.linspace(0,2*np.pi,n_phi)
r=np.linspace(0.01,2*n**2,n_r)

R,Theta,Phi=np.meshgrid(r,theta,phi)
psi=Ra(R,n,l)*Y(Theta,Phi,l,m)
psi=np.real(psi)

psi_p=np.where(psi>0,psi,0)
psi_n=np.where(psi<0,psi,0)
psi_n=abs(psi_n)


fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.set_title(f"Hydrogen obital with n={n}, l={l} and m={m}")

x,y,z=psi_p*np.sin(Theta)*np.cos(Phi),psi_p*np.sin(Theta)*np.sin(Phi),psi_p*np.cos(Theta)
x=x.reshape(n_r,n_theta*n_phi)
y=y.reshape(n_r,n_theta*n_phi)
z=z.reshape(n_r,n_theta*n_phi)

ax.plot_surface(x, y, z, cmap='BuGn', linewidth=0, alpha=0.3)

x,y,z=psi_n*np.sin(Theta)*np.cos(Phi),psi_n*np.sin(Theta)*np.sin(Phi),psi_n*np.cos(Theta)
x=x.reshape(n_r,n_theta*n_phi)
y=y.reshape(n_r,n_theta*n_phi)
z=z.reshape(n_r,n_theta*n_phi)

ax.plot_surface(x, y, z, cmap='viridis', linewidth=0, alpha=0.3)


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()