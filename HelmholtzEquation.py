import numpy as np
import matplotlib.pyplot as plt

# Define the problem domain
L = 1.0    # length of the domain
N = 100    # number of grid points
dx = L / (N-1)   # grid spacing
x = np.linspace(0, L, N)   # grid points
k = 2*np.pi / L   # wave number

# Define the boundary conditions
u0 = np.sin(k*x)   # boundary condition at x=0
uN = np.sin(k*x)   # boundary condition at x=L

# Set up the finite difference matrix
A = np.zeros((N, N))
for i in range(1, N-1):
    A[i, i-1] = 1/dx**2
    A[i, i] = -2/dx**2 - k**2
    A[i, i+1] = 1/dx**2
A[0, 0] = 1
A[N-1, N-1] = 1

# Solve the linear system
b = np.zeros(N)
b[0] = u0[0]
b[N-1] = uN[N-1]
u = np.linalg.solve(A, b)

# Plot the solution
plt.plot(x, u, label='Numerical solution')
plt.plot(x, np.sin(k*x), label='Exact solution')
plt.legend()
plt.xlabel('x')
plt.ylabel('u(x)')
plt.show()
