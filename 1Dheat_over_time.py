import numpy as np
import matplotlib.pyplot as plt

'''Geometry'''

l = 0.5                  #metre

'''Grid'''
n=0
dx=l/n    #float(input("Length of one division in metre "))

x=np.linspace(0,l,n)

'''Initial Comdition'''

T0 = 0                                                        #Cel   
T1s = 40 #int(input("Enter Left Surface Temperature: "))            #Cel
T2s = 20 #int(input("Enter Right Surface Temperature: "))           #Cel
T=np.ones(n)*T0                                                 #Vector Celcius

'''Defining other parameters'''

alpha=0.0001
t_final=int(input("Enter Total Time of Simulation: "))        #Sec
dt=float(input("Enter Time Step: "))                          #Sec
dt_check= 0.5*(dx**2)/(2*alpha)
if dt>dt_check:
    print("dt should be "+ str(dt_check))
    dt=dt_check


'''Solution Arrays'''

dTdt=np.zeros(n)            #LHS
t=np.arange(0,t_final,dt)   #time 

'''Simulation'''

for j in t:
    for i in range(1,n-1):
        dTdt[i]=alpha*(-(T[i]-T[i-1])/dx**2+(T[i+1]-T[i])/dx**2)
    dTdt[0]= alpha*(-(T[0]-T1s)/dx**2+(T[1]-T[0])/dx**2)
    dTdt[n-1]= alpha*(-(T[n-1]-T[n-2])/dx**2+(T2s-T[n-1])/dx**2)
    T=T+dTdt*dt
    T[0]=40
    T[-1]=20
plt.figure(1)
plt.plot(x,T)
# plt.axis([0,l,min(0,T1s,T2s), max(T1s,T2s)+10])
plt.xlabel("Distance")
plt.ylabel("Temperature")
plt.title("Temperature Profile over Time")
plt.show()
    

    
    
    
    
