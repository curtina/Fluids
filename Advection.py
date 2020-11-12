"""
1D Numerical Solution for Advection

author: Alice Curtin
date: November 5, 2020
"""

import numpy as np
import matplotlib.pyplot as plt

# defining initial values
N = 10 # number of values in our initial array of x-values which we then manipulate
steps = 100 # number of iterations to perform

dt = 1 # time step
dx = 0.3 # x step

u = -0.1 #initial veloicty

# setting up the initial x grid
xgrid = np.arange(N)*dx

# setting initial conditions for f which is the array that we will iteratively manipulate
f_ftcs = np.copy(xgrid)
f_lf = np.copy(xgrid)

# initiating an interactive plot
plt.ion()
fig, axes = plt.subplots(1,2)
axes[0].set_title("ftcs") # Forward-Time Central-Space Method
axes[1].set_title("lax-fried") # Lax-Friedrich method
x1,= axes[0].plot(xgrid, f_ftcs, 'bo')
x2, = axes[1].plot(xgrid, f_lf, 'bo')
axes[0].plot(xgrid, f_ftcs, "r")
axes[1].plot(xgrid, f_lf, "r")
axes[0].set_xlim(0,max(xgrid))
axes[0].set_ylim(0,N)
axes[1].set_xlim(0,max(xgrid))
axes[1].set_ylim(0,N)
fig.canvas.draw()
plt.pause(3)

# setting initial step
step_i = 0

# iterations of f based on advection
while step_i < steps:
    step_i +=1
    # Updating each step
    # Note that we run from 1 through N-1 so that we can use the two outer points for BCs
    # Forward-Time Central-Space Method
    f_ftcs[1:N-1] = f_ftcs[1:N-1] - u*dt/2/dx*(f_ftcs[2:] - f_ftcs[:N-2])
    # Lax-Friedrich method
    f_lf[1:N-1]  = 1/2*(f_lf[2:] + f_lf[:N-2]) - u*dt/2/dx*(f_lf[2:] - f_lf[:N-2])
    # updating the plot
    x1.set_ydata(f_ftcs)
    x2.set_ydata(f_lf)
    fig.canvas.draw()
    plt.pause(.1)
    
    