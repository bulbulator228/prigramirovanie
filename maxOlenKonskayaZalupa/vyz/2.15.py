import math
R = float(input("Введите внешний радиус: "))
r = float(input("Введите внутренний радиус: "))
S = math.pi * (R**2 - r**2)
print("Площадь кольца:", S)
