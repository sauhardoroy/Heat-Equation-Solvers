from matplotlib import pyplot as plt
import numpy as np

'''Geometry'''

x1=0.25              #1st block
x2=0.5             #2nd block

'''Spacial Grids'''
choice=int(input("Enter 1 for Coarse Mesh\nEnter 2 for Fine Mesh\nEnter 3 for Best Mesh\n"))
if choice==1:
    dx=0.05
elif choice==2:
    dx=0.01
else:
    dx=0.005
    
nx=int((x1+x2)/dx)+1
x=np.linspace(0,x1+x2,nx)
n1=int(x1/dx)

'''Time Grid'''

t_sim=int(input("Enter TIme of Simulation(in second): "))
dt=0.1
nt=int(t_sim/0.1)

'''Initial Conditions'''

T_ini=273.15+int(input("Enter Initial Temperature(in celsius): "))
T_heat=273.15+int(input("Enter Temperature of Heater(in celsius): "))

'''Material Properties'''

alpha1=0.00005
alpha2=0.000009

'''Result'''

T=np.ones(nx)*T_ini
T[n1]= T_heat

'''Simulation'''

for n in range (1,nt):
    plt.clf()
    Tn=T.copy()
    
    T[1:n1] = Tn[1:n1] + dt*alpha1*(Tn[0:n1-1] - 2*Tn[1:n1] + Tn[2:n1+1])/dx**2
    T[n1]=T_heat             #Boundary Cond 1 
    T[n1+1:-1] = Tn[n1+1:-1] + dt*alpha2*(Tn[n1:-2] - 2*Tn[n1+1:-1] + Tn[n1+2:])/dx**2
    T[0]=T[1]             #Boundary Cond 2
    T[-1]=T[-2]           #Boundary Cond 3
    
    if n%400 ==0:
        plt.figure(figsize=(6,7),dpi=100)
        plt.axis([0,x1+x2,0, 200])
        plt.plot(x,T-273.15,'k')
        plt.xlabel("Distance")
        plt.ylabel("Temperature (in Celcius)")
        plt.title("Temperature Profile after "+str(n*dt)+" Seconds")
        plt.show()
        plt.pause(0.01)















