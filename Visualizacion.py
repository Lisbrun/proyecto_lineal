import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

A = np.array([[2,4,6],[3,8,5],[-1,1,2]])
B = np.array([22,27,2])
sol = np.linalg.solve(A,B)
print(sol)
x,y = np.linspace(0,10,10),np.linspace(0,10,10)
X,Y = np.meshgrid(x,y)
z1 = (22-2*X-4*Y)/6
z2 = (27-3*X-8*Y)/5
z3 = (2+X-Y)/2
fig = plt.figure()
ax = fig.add_subplot (111, projection='3d')
ax.plot_surface(X,Y,z1, alpha= 0.5, cmap = cm.Accent, rstride=100, cstride=100)
ax.plot_surface(X,Y,z2, alpha= 0.5, cmap = cm.Paired, rstride=100, cstride=100)
ax.plot_surface(X,Y,z3, alpha= 0.5, cmap = cm.Pastel1, rstride=100, cstride=100)
ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
plt.show()