a = 0
b = 3
epsilon = 0.01

def f(x):
    return 3 * x**2 - 10 * x + 5

phi = (1 + 5**0.5) / 2  # Золотое сечение

while (b - a) / 2 > epsilon:
    x1 = b - (b - a) / phi
    x2 = a + (b - a) / phi
    if f(x1) < f(x2):
        b = x2
    else:
        a = x1

x_min = (a + b) / 2
print("Минимум функции:", x_min, f(x_min))
