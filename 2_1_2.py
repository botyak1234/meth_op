a = 0
b = 3
epsilon = 0.01

def f(x):
    return 3 * x**2 - 10 * x + 5

while (b - a) / 2 > epsilon:
    mid = (a + b) / 2
    left = mid - epsilon
    right = mid + epsilon
    if f(left) < f(right):
        b = right
    else:
        a = left

x_min = (a + b) / 2
print("Минимум функции:", x_min, f(x_min))
