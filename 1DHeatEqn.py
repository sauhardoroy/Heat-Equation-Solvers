import numpy as np
from matplotlib import pyplot as plt
import time

t1=time.time()

'''Geometry'''
s_B=0.5     #m

'''Spatical Grid'''

dx= 0.001    #m
nx= int(s_B/dx)+1
x=np.linspace(0, s_B,nx)

'''Material Properties'''

rho= 2000
cp= 500
lamda= 100
alpha=lamda/(rho*cp)

'''Time Grid'''

t_sim= 60      #sec
dt= 0.5

dt_check=0.5*(dx**2)/(2*alpha)
print(dt_check)
if dt>dt_check:
    print("dt should be "+str(dt_check))
    dt=dt_check
nt=int(t_sim/dt)


'''Initial Comdition'''
T_A= 273.15     #Kelvin

'''Define Result Parameter'''
T= np.ones(nx)*T_A
r=alpha*dt/(dx**2)


'''Simulation'''

for n in range (1,nt):
        Tn= T.copy()
        
        T[1:-1]=Tn[1:-1]+r*(Tn[2:]-2*Tn[1:-1]+Tn[0:-2])
        # for i in range (1,nx-1):
        #     T[i]=Tn[i]+r*(Tn[i+1]-2*Tn[i]+Tn[i-1])
        
        T[0] =313.15
        T[-1]= 293.15
# plotT= plt.figure(figsize=(6,7),dpi=100)
# plt.plot(x,T-273.15,'k')
# plt.show(plotT)
        if n%500==0 or n==nt-1:
            plt.figure(1)
            plt.plot(x,T-273.15)
# plt.axis([0,l,min(0,T1s,T2s), max(T1s,T2s)+10])
            plt.xlabel("Distance")
            plt.ylabel("Temperature")
            plt.title("Temperature Profile over Time")
            plt.show()
t2=time.time()
print(t2-t1)