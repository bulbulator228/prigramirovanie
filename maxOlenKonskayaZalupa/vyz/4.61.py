import math
a, b, c = map(float, input("Введите a, b, c (a ≠ 0): ").split())
D = b**2 - 4*a*c
if D > 0:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print("Два корня:", x1, x2)
elif D == 0:
    x = -b / (2*a)
    print("Один корень:", x)
else:
    print("Корней нет (действительных)")
