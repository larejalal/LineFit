from fitting_functions import *

### Test 1: linear
print("Testing linear:")
print(linear(2, 3, 4))

### Test 2: slope_units
print("Testing slope_units:")
print(slope_units("meters", "kg"))
print(slope_units("sec", "meters"))

### Test 3: print_equation
print("Testing print_equation:")
print_equation(4, 1, "kg", "meters")
