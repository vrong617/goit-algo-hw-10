import numpy as np
import scipy.integrate as integrate

def function(x):
    return x**3


def monte_carlo_integration(f, a, b, num_samples=10000):
    x_random = np.random.uniform(a, b, num_samples)
    y_values = f(x_random)
    integral_value = (b - a) * np.mean(y_values)
    return integral_value


def analytical_integration(f, a, b):
    integral_value, error = integrate.quad(f, a, b)
    return integral_value


a, b = 0, 1

monte_carlo_result = monte_carlo_integration(function, a, b, num_samples=100000)
analytical_result = analytical_integration(function, a, b)

print(f"Інтеграл методом Монте-Карло: {monte_carlo_result}")
print(f"Аналітичне значення інтеграла (quad): {analytical_result}")
print(f"Похибка: {abs(monte_carlo_result - analytical_result)}")
