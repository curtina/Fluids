"""
1D Numerical Solution for the Hydrodynamic Continuity and Euler equations after a slight Gaussian perturbation to the initial density

author: Alice Curtin
date: November 11, 2020
"""

import numpy as np
import matplotlib.pyplot as plt

# defining initial values
N = 100 # number of values in our initial array of x-values which we then manipulate
steps = 200 # number of iterations

# defining initial coefficients
dt = 0.2 # time step
dx = 0.7 # x step
cs2 = 6# sound speed which is assumed to be constant 

# setting up the initial x grid
xgrid = np.arange(N)*dx

# setting initial conditions for f1 and f2
# f1 is the density
# f2 is the density * velocity
# perturbing both the density by a gaussian
rho0 = 1
mu = max(xgrid)/2
sigma = 3
f1 = rho0 + 0.1*np.exp(-(xgrid-mu)**2/2/sigma**2)
f2 = 0.1*np.exp(-(xgrid-mu)**2/2/sigma**2)

# initiating an interactive plot
plt.ion()
fig, axes = plt.subplots(1,1)
axes.set_title("density")
x1, = axes.plot(xgrid, f1, 'bo')
fig.canvas.draw()
plt.pause(1)

# setting initial step to be 0
step_i = 0

# need time step short enough for sound waves to transfer

# starting iterations of f1 and f2
while step_i < steps:
    # Updating each step
    step_i +=1
    
    # computing velocity
    # velocity is N+1 dimensions 
    #u = np.zeros(len(f1)+1)
    J1 = np.zeros(N+1)
    J2 = np.zeros(N+1)  
    
    # updating velocity and flux
    for i in range(1,N):
        u = 1/2*(f2[i-1]/f1[i-1] + f2[i]/f1[i])
        if f1[i] < 0:
            print(f1[i])
            print(f1[i-1])
        if u > 0:
            J1[i] = u*f1[i-1]
            J2[i] = u*f2[i-1]
        if u < 0:
            J1[i] = u*f1[i]
            J2[i]= u*f2[i]                
    # getting final value for f1
    f1 = f1 - dt/dx*(J1[1:]-J1[:-1])
    
    # Apply BCs for f1
    f1[0] = f1[0] - (dt / dx) * J1[0]
    f1[-1] = f1[-1] + (dt / dx) * J1[-2]
    
    # getting final value for f2
    f2 = f2 - dt/dx*(J2[1:]-J2[:-1]) 
    
    # Accounting for pressure
    f2[1:-1] = f2[1:-1] - dt/dx*cs2*(f1[2:]-f1[:-2])
    
    # Apply BCs for f2
    f2[0] = f2[0] - (dt / dx) * J2[0]
    f2[-1] = f2[-1] + (dt / dx) * J2[-2]
    
    x1.set_ydata(f1)
    #x2.set_ydata(f2)
    fig.canvas.draw()
    plt.show()
    plt.pause(.1)