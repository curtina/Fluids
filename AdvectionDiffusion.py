"""
1D Numerical Solution for the Advection-Diffusion Equation

Outline:
1. Define initial variables including number of grid points, number of iterations, time step, grid step, diffusion coefficients, matrices for solving the diffusion equation, initial velocity
2. Initiate two plots
3. Iteratively update the f using the FTCS and Lax-Friedrich methods

author: Alice Curtin
date: November 12, 2020
"""

import numpy as np
import matplotlib.pyplot as plt

# defining initial values
N = 100 # number of values in our initial array of x-values which we then manipulate
steps = 500 # number of iterations to perform

# Setting initial conditions on dt, dx, u
# Note that we need dx/dt > u for stability with the Lax-Friedrich method
dt = 1 # time step
dx = 0.3 # x spacing
u = -0.1 # initial velocity
D1 = 1.0 # first diffusion coefficient
D2 = 0.1 # second diffusion coefficient

# Defining a matrix for solving the diffusion equation using the implicit method
beta1 = D1*dt/(dx)**2 # defining a factor beta for the matrix
A1 = np.eye(N) * (1.0 + 2.0*beta1) + np.eye(N, k=1)*-beta1 + np.eye(N, k=-1)*-beta1 # matrix for handling the diffusion term

# Applying no-slip BCs
A1[0][0] = 1 
A1[0][1] = 0
A1[-1][-1] = 1
A1[-1][-2] = 0

# Defining a second matrix for the second diffusion coefficient
beta2 = D2*dt/(dx)**2 # second beta
A2 = np.eye(N) * (1.0 + 2.0*beta2) + np.eye(N, k=1)*-beta2 + np.eye(N, k=-1)*-beta2 # second matrix

# Applying no-slip BCS
A2[0][0] = 1 
A2[0][1] = 0
A2[-1][-1] = 1
A2[-1][-2] = 0

# setting up the initial x grid
xgrid = np.arange(N)*dx

# setting initial conditions for f1 and f2 which correspond to diffusion coefficients D1 and D2
f1 = xgrid
f2= xgrid

# initiating an interactive plot
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
axes[1].set_ylim(0,N)
axes[0].set_ylabel("f")
axes[0].set_xlabel("Arbitrary Spatial coordinate")
axes[1].set_xlabel("Arbitrary Spatial coordinate")
fig.canvas.draw()
plt.pause(0.05)

# setting initial step
step_i = 0

# iterations of f1 and f2 based on advection AND diffusion
while step_i < steps:
    step_i +=1 # updating each step
    # Solving for diffusion result using our matrix A1
    f1 = np.linalg.solve(A1, f1)
    # Combining the diffusion result with our advection code presented in Advection.py
    f1[1:N-1] = 1/2*(f1[2:] + f1[:N-2]) - u*dt/2/dx*(f1[2:] - f1[:N-2]) 
    # Different diffusion coefficient
    # Solving for the diffusion result using our matrix A2
    f2 = np.linalg.solve(A2, f2) 
    # Combining the diffusion result with our advection code presented in Advection.py
    f2[1:N-1] = 1/2*(f2[2:] + f2[:N-2]) - u*dt/2/dx*(f2[2:] - f2[:N-2])
    # updating the plot
    x1.set_ydata(f1)
    x2.set_ydata(f2)
    fig.canvas.draw()
    plt.show()
    plt.pause(.05)
    