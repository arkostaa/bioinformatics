import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Определяем правую часть системы уравнений
def equations(state, t, A, a, h, beta):
    z, y, x = state
    if z > beta:
        dzdt = y - a*A
    else:
        dzdt = 0  # если z <= beta, производная z равна 0
    dydt = (1/a) * (z - 2*h*a*y - (1+a)*x)
    dxdt = y
    return [dzdt, dydt, dxdt]

# Устанавливаем начальные условия
A = 1  # пример значения для A
a = 0.5  # пример значения для a
h = 0.2  # пример значения для h
beta = 0  # пример значения для beta
state0 = [1, 2, 3]  # начальные значения z, y и x
t = np.linspace(0, 10, 1000)  # массив значений времени

# Решаем систему дифференциальных уравнений
states = odeint(equations, state0, t, args=(A, a, h, beta))

# Визуализируем результаты
plt.plot(t, states[:, 0], 'b', label='z(t)')  # график z от t
plt.plot(t, states[:, 1], 'r', label='y(t)')  # график y от t
plt.plot(t, states[:, 2], 'g', label='x(t)')  # график x от t
plt.xlabel('Time')
plt.ylabel('Values')
plt.legend()
plt.show()