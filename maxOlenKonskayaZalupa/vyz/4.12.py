import math
r = float(input("Введите радиус круга: "))
a = float(input("Введите сторону квадрата: "))
circle_area = math.pi * r * r
square_area = a * a
if circle_area > square_area:
    print("Площадь круга больше")
else:
    print("Площадь квадрата больше")
