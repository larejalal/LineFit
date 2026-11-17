import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.stats import norm
from fitting_functions import print_equation
### EXERCISE 1

print("Running the spring experiment")
data = np.loadtxt("spring2.csv", delimiter=",", dtype=str)
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

plt.savefig("spring_graph2.png")
plt.show()
'''
Comparison of Exercise 1 and Exercise 2

Exercise 1:
F = 200d

Exercise 2:
F = 300d - 0.010 (approximately)

Both equations show a linear relationship between
force and displacement.

Exercise 2 has a larger slope because the spring
constant increased from 200 N/m to 300 N/m.
This means more force is needed to stretch the
spring by the same distance.

Both intercepts are approximately zero.
'''
