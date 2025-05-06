
#%% U1
s1=0
s2=0
n=0

while 1:
    n=n+1
    s1=s1+1/n
    s2=s2+1/n**3
    p=s1*s2
    if p<= 3.8:
        if 3.5 <= p:
            print(n)
    else:
        break
#%% U2

import numpy as np
def perm(vec):
    n=len(vec)
    n=n-n%2
    ut=np.zeros(n)
    for k in range(0,n,2):
        v=vec[k:k+2]
        ut[k]=min(v)
        ut[k+1]=max(v)
    return ut

#%% U3
import numpy as np
def pos_int(M):
    return np.all(M>0) and np.all(np.round(M)==M)

#%% U4
import numpy as np
import matplotlib.pyplot as plt

ax=plt.axes(projection='3d')
phi=np.linspace(0,2*np.pi,30)
ax.plot3D(np.cos(phi),np.sin(phi),np.ones(30))
ax.plot3D(np.cos(phi),np.sin(phi),-np.ones(30))
phi=np.linspace(0,2*np.pi,11)
phi=phi[0:-1]
for k in range(10):
    x=np.cos(phi[k])
    y=np.sin(phi[k])
    ax.plot3D([-x,x],[-y,y],[-1,1],'k-')

#%% U5
def sum_files():
    L=os.listdir()
    summor=[]
    for l in L:
       s=0
       with open(l,'r') as fid:
          Li=fid.readlines()
          for li in Li:
              s=s+int(li)
          summor=summor + [s]
    with open('sums.dat','w') as fid:
        for s in summor:
           fid.write(str(s)+'\n')
        
#%% U6
from sympy import isprime
from math import sqrt
n=2
no_of_p=0
prev_p=0
while no_of_p<10:
    n=n+1
    if isprime(n):
        s2=int(sqrt(n))
        for p in range(1,s2+1):
            for q in range(p,s2+1):
                for r in range(q,s2+1):
                    if n==p**2+q**2+r**2 and n != prev_p:
                        print(n,p,q,r)
                        no_of_p=no_of_p+1
                        prev_p=n
