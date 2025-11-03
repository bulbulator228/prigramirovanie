import math
n = 1000
dy = (2 - 1) / n
area = 0
for i in range(n):
    y = 1 + i * dy
    x_left = -2 - math.sqrt((y - 1) / 0.4)
    x_right = -2 + math.sqrt((y - 1) / 0.4)
    width = x_right - x_left
    area += width * dy
print(f"Приблизительная площадь: {area:.4f}")