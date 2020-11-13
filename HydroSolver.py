"""
1D Numerical Solution for the Hydrodynamic Continuity and Euler equations after a slight Gaussian perturbation to the initial density (assuming no gravity) and velocity

Outline:
1. Define initial variables including number of grid points, number of iterations, time step, grid step, sound speed, rho0
2. Add a gaussian perturbation to our density (and velocity)
3. Iteratively calculate the u (velocity) and J (flux) for rho and rho*u at the cell interfaces
4. Use u and J to progress rho and rho*u in time.
5. Add the source term for rho*u of -dP/dx (P=pressure).

author: Alice Curtin
date: November 12, 2020
"""
import numpy as np
import matplotlib.pyplot as plt

# defining initial values
N = 100 # number of values in our initial array of x-values which we then manipulate
steps = 120 # number of iterations

# defining initial coefficients
# note that we need dx/dt < cs2
dt = 0.2 # time step
dx = 0.4 # x step
cs2 = 6 # sound speed squared which is assumed to be constant 

# setting up the initial x grid
xgrid = np.arange(N)*dx

# setting initial conditions for f1 and f2
# f1 is the density
# f2 is the density * velocity
# perturbing the density by a gaussian in both f1 and f2 along with the velocity
rho0 = 3
mu = np.mean(xgrid)
sigma = 3
# amplitude = 0.05 is a small perturbation while amplitude = 0.3 results in a large perturbation
amplitude = 0.3
f1 = rho0 + amplitude*np.exp(-(xgrid-mu)**2/2/sigma**2)
# setting initial velocity =0 and not perturbing it
u = np.zeros(N)
f2 = f1*u
# Below is code if we want to also perturb u
#f2=f1*(0.05*np.exp(-(xgrid-mu)**2/2/sigma**2))

# initiating an interactive plot of the density
plt.ion()
fig, axes = plt.subplots(1,1)
axes.set_title("density")
axes.plot(xgrid, f1, 'r')
x1, = axes.plot(xgrid, f1, 'b')
#axes.set_ylim(0.9,1.5)
fig.canvas.draw()
plt.pause(1)

# setting initial step to be 0
step_i = 0


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
        u = 1/2*(f2[i-1]/f1[i-1] + f2[i]/f1[i]) # velocity
        if u > 0:
            J1[i] = u*f1[i-1] #flux
            J2[i] = u*f2[i-1] #flux
        if u < 0:
            J1[i] = u*f1[i]
            J2[i]= u*f2[i]    
            
    # evolving f1
    f1 = f1 - dt/dx*(J1[1:]-J1[:-1])
    
    # Apply BCs for f1
    f1[0] = f1[0] - (dt / dx) * J1[0]
    f1[-1] = f1[-1] + (dt / dx) * J1[-2]
    
    # evolving f2
    f2 = f2 - dt/dx*(J2[1:]-J2[:-1]) 
    
    # Accounting for pressure
    f2[1:-1] = f2[1:-1] - dt/dx*cs2*(f1[2:]-f1[:-2])
    
    # Apply BCs for f2
    f2[0] = f2[0] - (dt / dx) * J2[0]
    f2[-1] = f2[-1] + (dt / dx) * J2[-2]
    
    # updating plot
    x1.set_ydata(f1)
    fig.canvas.draw()
    plt.show()
    plt.pause(.1)