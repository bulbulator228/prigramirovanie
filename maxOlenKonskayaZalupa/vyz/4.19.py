import math
circle_area = float(input("Площадь круга: "))
triangle_area = float(input("Площадь равностороннего треугольника: "))
radius = math.sqrt(circle_area / math.pi)
a = math.sqrt((4 * triangle_area) / math.sqrt(3))
r_in = a * math.sqrt(3) / 6
r_out = a * math.sqrt(3) / 3
# а)
if radius <= r_in:
    print("Круг уместится в треугольнике")
else:
    print("Круг не уместится в треугольнике")
# б)
if a <= 2 * radius:
    print("Треугольник уместится в круге")
else:
    print("Треугольник не уместится в круге")
