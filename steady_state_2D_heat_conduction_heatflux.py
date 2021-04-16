import numpy as np
from matplotlib import pyplot as plt

'''Geometry'''
x_B      = 0.03       #m
y_B      = 0.03       #m

'''Spacial Grids'''
n=int(input("Enter Number of Grids in X and Y direction: "))
x        = np.linspace(0,x_B,n)
y        = np.linspace(0,y_B,n)
h=x[1]-x[0]
X, Y = np.meshgrid(x, y)

'''Boundary Conditions'''           #Celsius
T_top    = int(input("Enter Temperatur at Top Surface(in celsius): "))
T_bottom = int(input("Enter Temperatur at Bottom Surface(in celsius): "))
T_left   = int(input("Enter Temperatur at Left Surface(in celsius): "))
T_right  = int(input("Enter Temperatur at Right Surface(in celsius): "))

'''Result Parameter'''
T        = np.zeros((n,n),dtype='float64')


T[:,0]   = T_left
T[:,-1]  = T_right
T[0,:]   = T_top
T[-1,:]  = T_bottom

tol      = 1e-6
error    = 1  
k=0

xs=np.array([])
ys=np.array([])

'''Simulation'''

while (error > tol):
    k+=1
    T_old = T.copy()
    for i in range (1,n-1):
        for j in range (1,n-1):
            T[i,j]=0.25*(T[i,j-1]+T[i-1,j]+T[i+1,j]+T[i,j+1])
    T_error=abs(T_old[1:-1]-T[1:-1])
    error=np.amax(T_error)
    
    xs=np.append(xs,k)
    ys=np.append(ys,error)
    #if(k%40==0):
        #plt.plot(xs,ys)
        #plt.xlabel("Number of Iteration")
        #plt.ylabel("Error")
       # plt.show()

qx=np.zeros((n,n),dtype='float64')
qy=np.zeros((n,n),dtype='float64') 
for i in range (1,n-1):
    for j in range (1,n-1):
        qx[i,j]=-(T[i+1,j]-T[i-1,j])/(2*h)
        qy[i,j]=-(T[i,j+1]-T[i,j-1])/(2*h)  
    
plt.clf()   
'''Plotting'''



fig2, ax2 = plt.subplots()
q = ax2.quiver(x.T, y, qx.T,qy.T)

mycmap1 = plt.get_cmap('viridis')

fig,ax=plt.subplots()

cp=ax.contourf(x, y, T, cmap=mycmap1)


fig.colorbar(cp,ax=ax)                            # Add a colorbar to a plot

ax.set_title('Temperature Contours')
ax.set_xlabel('x (m)')
ax.set_ylabel('y (m)')
plt.imshow(T,interpolation='gaussian')
plt.show()



print("Error = "+ str(error))
print("Number of iterations= "+str(k-1))