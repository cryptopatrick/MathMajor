# Lösningsförslag tenta 2022-06-09
"""
import numpy as np
import matplotlib.pyplot as plt

# U1
a=-1; b=1; n=100
h=(b-a)/n
q=0
for i in range(n):
    x=a+i*h
    q=q+np.exp(-x**2)
print(q)

# U2
def ydot(a,b):
    C=np.zeros([np.size(a),np.size(b)])
    for i in range(np.size(a)):
        for j in range(np.size(b)):
            C[i,j]=a[i]*b[j]
    return C

# U3   
def ymul(A,B):
    (m,k)=np.shape(A)
    (kb,n)=np.shape(B)
    if k!= kb:
        return []
    C=np.zeros([m,n])
    for i in range(k):
        C=C+ydot(A[:,i],B[i,:])
    return C

# U4
x=np.linspace(-1,1,2)
y=np.linspace(-1,1,2)
X, Y = np.meshgrid(x,y)
Z=2*X-2*Y
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z)


t=np.linspace(0,1)
ax.plot3D(2*t,-2*t,0)
ax.plot3D(2,2,0,'ko')

# U5
def tyo_o_liksom(filnamn):
    typ=0; liksom=0
    with open(filnamn,'r') as fid:
        l=fid.readlines()
    for wrd in l:
        if wrd=="typ\n":
            typ=typ+1
        elif wrd=="liksom\n":
            liksom=liksom+1
    return typ,liksom
           
           
# U6
from sympy import isprime
def uppg6():
    found=0
    n=0
    while found<15:
        n=n+1
        v=[]
        for j in range(1,n+1):
            if n%j==0:
                v=v+[j]
        if isprime(sum(v)):
            found=found+1
            print(n)
