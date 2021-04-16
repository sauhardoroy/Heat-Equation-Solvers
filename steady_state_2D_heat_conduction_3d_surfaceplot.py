from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

'''Geometry'''
x_B      = 0.03       #m
y_B      = 0.03       #m

'''Spacial Grids'''
n=int(input("Enter Number of Grids in X and Y direction: "))
x        = np.linspace(0,x_B,n)
y        = x.copy().T
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
    
    if(k%40==0):
        plt.plot(xs,ys)
    
        plt.xlabel("Number of Iteration")
        plt.ylabel("Error")
        plt.show()

        
            
    
plt.clf()   
'''Plotting'''

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, T, cmap=cm.viridis,
                       linewidth=0, antialiased=False)
ax.set_zlim(min(T_top,T_bottom,T_left,T_right),max(T_top,T_bottom,T_left,T_right))
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
                          
fig.colorbar(surf, shrink=0.5, aspect=5)


ax.set_title('Temperature Contours')
ax.set_xlabel('x (m)')
ax.set_ylabel('y (m)')

plt.show()



print("Error = "+ str(error))
print("Number of iterations= "+str(k-1))