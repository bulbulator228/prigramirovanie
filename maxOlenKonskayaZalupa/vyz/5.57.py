import math
def x_for_y(y):
    return 1 +- math.sqrt((y - 3) / 0.3)  # ищем x по y
# Для y=2
delta = math.sqrt((2 - 3) / 0.3)
x_left = 1 - delta
x_right = 1 + delta

# для y=4
delta2 = math.sqrt((4 - 3) / 0.3)
x_left2 = 1 - delta2
x_right2 = 1 + delta2
n = 1000
dy = (4 - 2) / n
area = 0

for i in range(n):
    y = 2 + i * dy
    delta_y = math.sqrt((y - 3) / 0.3)
    x_left = 1 - delta_y
    x_right = 1 + delta_y
    width = x_right - x_left
    area += width * dy

print(f"Приблизительная площадь: {area:.4f}")