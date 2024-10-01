import numpy as np

def f(x):
    return x**3 + 3*x**2 - 3*x + 1

def method_of_parabolas(x0, x1, x2, epsilon=1e-5, max_iter=100):
    for _ in range(max_iter):
        f0, f1, f2 = f(x0), f(x1), f(x2)

        # Коэффициенты параболы
        a = ((f2 - f0) * (x1 - x0) - (f1 - f0) * (x2 - x0)) / ((x2 - x0) * (x1 - x0) * (x2 - x1))
        b = ((f1 - f0) * (x2 - x0) - (f2 - f0) * (x1 - x0)) / ((x2 - x0) * (x1 - x0) * (x2 - x1))
        c = f0 - a * x0**2 - b * x0

        # Минимум параболы
        x_min = -b / (2 * a)

        # Проверка условия завершения
        if abs(x_min - x1) < epsilon:
            break

        # Замена одной из точек
        if x_min < x1:
            if f(x_min) < f(x0):
                x2, x1, x0 = x1, x0, x_min
            else:
                x2, x1 = x1, x_min
        else:
            if f(x_min) < f(x2):
                x0, x1, x2 = x1, x2, x_min
            else:
                x0, x1 = x1, x_min

    return x_min, f(x_min)

# Начальные точки
x0, x1, x2 = 0, 1, 2

# Нахождение минимума
x_min, f_min = method_of_parabolas(x0, x1, x2)
print("Минимум функции:", x_min, f_min)
