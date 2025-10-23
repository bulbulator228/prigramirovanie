import math
x = float(input("Введите значение x: "))
if x > 0:
    y = math.sin(x**2)
else:
    y = 1 - 2 * math.sin(x)**2
print(f"Значение y: {y}")
