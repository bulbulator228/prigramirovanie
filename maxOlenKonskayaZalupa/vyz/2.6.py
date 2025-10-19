import math
R = 6350
h = float(input("Введите высоту над землей (в км): "))
d = math.sqrt(2 * R * h)
print("Расстояние до горизонта:", d, "км")