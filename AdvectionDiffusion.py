import numpy as np
import matplotlib.pyplot as plt

N = 100
steps = 1000

# coefficients
dt = 1
dx = 0.3
u = -0.1
D1 = 0.001
beta1 = D1*dt/(dx)**2
A1 = np.eye(N) * (1.0 + 2.0*beta1) + np.eye(N, k=1)*-beta1 + np.eye(N, k=-1)*-beta1
D2 = 0.1
beta2 = D2*dt/(dx)**2
A2 = np.eye(N) * (1.0 + 2.0*beta2) + np.eye(N, k=1)*-beta2 + np.eye(N, k=-1)*-beta2


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
    f1 = np.linalg.solve(A1, f1)
    f1[1:N-1] = 1/2*(f1[2:] + f1[:N-2]) - u*dt/2/dx*(f1[2:] - f1[:N-2])
    
    # different diffusion coefficient
    f2 = np.linalg.solve(A2, f2)
    f2[1:N-1] = 1/2*(f2[2:] + f2[:N-2]) - u*dt/2/dx*(f2[2:] - f2[:N-2])
    
    x1.set_ydata(f1)
    x2.set_ydata(f2)
    fig.canvas.draw()
    plt.show()
    plt.pause(.05)
    