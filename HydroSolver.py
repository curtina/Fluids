import numpy as np
import matplotlib.pyplot as plt

N = 5
steps = 2

# coefficients
dt = 1
dx = 0.3

# setting up the initial x grid
xgrid = np.arange(N)*dx

# setting initial conditions for f
f1 = xgrid
f2= xgrid

# initiating plot
plt.ion()
fig, axes = plt.subplots(1,2)
axes[0].set_title("D=" + str(D1))
axes[1].set_title("D="+str(D2))
x1,= axes[0].plot(xgrid, f1, 'bo')
x2, = axes[1].plot(xgrid, f2, 'bo')
axes[0].plot(xgrid, f1, "r")
axes[1].plot(xgrid, f2, "r")
axes[0].set_xlim(0,max(xgrid))
axes[0].set_ylim(0,N)
axes[1].set_xlim(0,max(xgrid))
axes[1].set_ylim(0,N)
fig.canvas.draw()
plt.pause(1)

step_i = 0

while step_i < steps:
    step_i +=1
    # Updating each step
    # Note that we run from 1 through N-1 so that we can use the two outer points for BCs
    #f[1:N-1]  = 1/2*(f[2:] + f[:N-2]) - u*dt/2/dx*(f[2:] - f[:N-2])
    u+=1/2*(f2/f1)
    u+[1:N]+=1/2* (f2[1:N]/f1[1:N])
    
    u- = 1/2*(f2/f1)
    u-[0:N-1] += 1/2*(f2[0:N-1]/f1[0:N-1])
    
    J1+ = []
    J1- =[]
    J2+ []
    J2- []
    for u in u+:
        if u > 0:
            J1+ = 
            J2+ = 
        else:
            J1+ = 
            J2+ = 
            
    for u in u-:
        if u > 0:
            J1- = 
            J2- =      
        else:
            J1- = 
            J2- =  

    
    
    x1.set_ydata(f1)
    x2.set_ydata(f2)
    fig.canvas.draw()
    plt.show()
    plt.pause(.05)