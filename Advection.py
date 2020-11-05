import numpy as np
import matplotlib.pyplot as plt

N = 10
steps = 100

dt = 1
dx = 0.3

u = -0.1

# setting up the initial x grid
xgrid = np.arange(N)*dx

# setting initial conditions for f
f_ftcs = np.copy(xgrid)
f_lf = np.copy(xgrid)

# initiating plot
plt.ion()
fig, axes = plt.subplots(1,2)
axes[0].set_title("ftcs")
axes[1].set_title("lax-fried")
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

step_i = 0

while step_i < steps:
    step_i +=1
    # Updating each step
    # Note that we run from 1 through N-1 so that we can use the two outer points for BCs
    f_ftcs[1:N-1] = f_ftcs[1:N-1] - u*dt/2/dx*(f_ftcs[2:] - f_ftcs[:N-2])
    f_lf[1:N-1]  = 1/2*(f_lf[2:] + f_lf[:N-2]) - u*dt/2/dx*(f_lf[2:] - f_lf[:N-2])
    x1.set_ydata(f_ftcs)
    x2.set_ydata(f_lf)
    fig.canvas.draw()
    plt.show()
    plt.pause(.1)
    
    