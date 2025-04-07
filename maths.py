import numpy as np
import matplotlib.pyplot as plt

N = 100
q = 0.95

x_values = np.linspace(1, 150, 1000)
test_counts = N * (1 - q ** x_values + 1 / x_values)

min_tests = np.min(test_counts)
optimal_x = x_values[np.argmin(test_counts)]

print(f"Optimal group size x: {optimal_x:.2f}")
print(f"Minimum average number of tests: {min_tests:.2f}")

plt.plot(x_values, test_counts)
plt.xlabel("Group Size x")
plt.ylabel("Average Number of Tests")
plt.title("Blood Testing Optimization")
plt.grid(True)
plt.show()
