import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

# Функція для інтегрування
def f(x):
    return x ** 2

# Межі інтегрування
a = 0
b = 2

# ----- Монте-Карло інтегрування -----
def monte_carlo_integral(f, a, b, num_samples=100000):
    x_rand = np.random.uniform(a, b, num_samples)
    y_rand = f(x_rand)
    area = (b - a) * np.mean(y_rand)
    return area

# ----- Обчислення інтеграла -----
mc_result = monte_carlo_integral(f, a, b)
quad_result, quad_error = spi.quad(f, a, b)

# ----- Вивід результатів -----
print(f"Метод Монте-Карло: {mc_result:.6f}")
print(f"Quad (точний):     {quad_result:.6f}, похибка: {quad_error:.6e}")

# ----- Побудова графіка -----
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)

ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title(f'Графік інтегрування f(x) = x^2 від {a} до {b}')
plt.grid()
plt.show()