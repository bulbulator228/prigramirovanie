import math
a = float(input("Введите первый катет: "))
b = float(input("Введите второй катет: "))
c = math.sqrt(a**2 + b**2)
P = a + b + c
print("Периметр треугольника:", P)
