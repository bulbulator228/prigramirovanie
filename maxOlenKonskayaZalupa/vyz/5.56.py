import math
a = 0
b = math.pi
n = 1000  # число разбиений
h = (b - a) / n
area = 0
for i in range(n):
    x1 = a + i * h
    x2 = x1 + h
    y1 = math.sin(x1)
    y2 = math.sin(x2)
    area += (y1 + y2) / 2 * h
print(f"Приблизительная площадь арки: {area:.4f}")