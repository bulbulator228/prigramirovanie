import math
a = float(input("Введите коэффициент a (≠ 0): "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))
D = b*b - 4*a*c
if D >= 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print(f"Корни уравнения: x1 = {x1}, x2 = {x2}")
else:
    print("Корней нет")
