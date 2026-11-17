import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.stats import norm
from fitting_functions import print_equation
### EXERCISE 1

print("Running the spring experiment")

data = np.loadtxt("data_fixed.csv", delimiter=",", dtype=str)

print(data[0])
d = data[1:, 0].astype(np.float32)
f = data[1:, 1].astype(np.float32)

print("Displacement:", d)
print("Force:", f)

def linear(x, m, b):
    return m * x + b

params, params_cov = scipy.optimize.curve_fit(linear, d, f)

slope = params[0]
intercept = params[1]

print("Slope:", slope)
print("Intercept:", intercept)
print("Equation: F =", slope, "* d +", intercept)
print_equation(slope, intercept, "N", "meters")
### Plot Exercise 1

plt.scatter(d, f, label="Spring Data")

plt.plot(d, linear(d, slope, intercept),
         label="Best-Fit Line")

plt.xlabel("Displacement (m)")
plt.ylabel("Applied Force (N)")
plt.title("Spring Force vs. Displacement")
plt.legend()
plt.grid(True)

plt.savefig("spring_graph.png")
plt.show()

