import math
x1, y1 = map(float, input("Введите координаты вершины 1 (x1 y1): ").split())
x2, y2 = map(float, input("Введите координаты вершины 2 (x2 y2): ").split())
x3, y3 = map(float, input("Введите координаты вершины 3 (x3 y3): ").split())

def dist(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

a = dist(x1, y1, x2, y2)
b = dist(x2, y2, x3, y3)
c = dist(x3, y3, x1, y1)

perimeter = a + b + c
p = perimeter / 2  # полупериметр
area = math.sqrt(p * (p - a) * (p - b) * (p - c))

print("Периметр треугольника:", perimeter)
print("Площадь треугольника:", area)