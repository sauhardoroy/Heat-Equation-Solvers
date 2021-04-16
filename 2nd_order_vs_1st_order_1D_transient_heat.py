import numpy as np
from matplotlib import pyplot as plt
import time

t1=time.time()

'''Geometry'''
s_B=0.5     #m

'''Spatical Grid'''

dx= 0.005    #m
nx= int(s_B/dx)+1
x=np.linspace(0, s_B,nx)

'''Time Grid'''

t_sim= 60      #sec
dt= 0.1
nt=int(t_sim/dt)

'''Material Properties'''

rho= 2000
cp= 500
lamda= 100
alpha=lamda/(rho*cp)

'''Initial Comdition'''
T_A= 273.15     #Kelvin

'''Define Result Parameter'''
T1= np.ones(nx)*T_A
T2= np.ones(nx)*T_A
Tn1= T1.copy()
Tn2= T2.copy()
r=alpha*dt/(dx**2)

'''Simulation'''

for n in range (1,nt):
        

        # for i in range (1,nx-1):
            
        #     T1[i] = ((1-2*r)*Tn1[i] + r*Tn1[i+1] + r*Tn1[i-1]+r*T1[i+1]+r*T1[i-1])/(1+2*r)    #crank-nicholson

        #     T2[i]=Tn2[i]+r*(Tn2[i+1]-2*Tn2[i]+Tn2[i-1])               #finite difference
        Tn1[1:-1] = ((1-2*r)*T1[1:-1] + r*T1[2:] + r*T1[0:-2]+r*Tn1[2:]+r*Tn1[0:-2])/(1+2*r)
        Tn2[1:-1]=T2[1:-1]+r*(T2[2:]-2*T2[1:-1]+T2[0:-2])
        
        T1= Tn1.copy()
        T2= Tn2.copy()
        
        Tn1[0] =313.15
        Tn1[-1]= 293.15
        Tn2[0] =313.15
        Tn2[-1]= 293.15


plt.figure(figsize=(6,7),dpi=100)
plt.plot(x,Tn1-273.15,label='Second Order Accurate')
plt.plot(x,Tn2-273.15,label='First Order Accurate')

plt.legend()
plt.xlabel("Distance")
plt.ylabel("Temperature")
plt.title("Temperature Profile over Time")
plt.show()

t2=time.time()
print(t2-t1)