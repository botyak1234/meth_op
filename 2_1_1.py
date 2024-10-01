x = 1.5
delta_x = 0.1

def f(x):
    return 3 * x**2 - 10 * x + 5

while True:
    f_current = f(x)
    f_next = f(x + delta_x)
    if f_next < f_current:
        x += delta_x
    else:
        break

print("Минимум функции:", x, f(x))
