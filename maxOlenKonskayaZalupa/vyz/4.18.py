import math
circle_area = float(input("Площадь круга: "))
square_area = float(input("Площадь квадрата: "))
radius = math.sqrt(circle_area / math.pi)
side = math.sqrt(square_area)
# а)
if 2*radius <= side:
    print("Круг уместится в квадрате")
else:
    print("Круг не уместится в квадрате")
# б
square_diag = side * math.sqrt(2)
circle_diameter = 2 * radius
if square_diag <= circle_diameter:
    print("Квадрат уместится в круге")
else:
    print("Квадрат не уместится в круге")
