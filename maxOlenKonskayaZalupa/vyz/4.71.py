import math
alpha_deg = float(input("Введите угол α (в градусах): "))
v0 = float(input("Введите начальную скорость v0 (м/с): "))
R = float(input("Введите высоту цели R (м): "))
g = 9.8  # ускорение свободного падения, м/с²
alpha = math.radians(alpha_deg)
H = (v0**2 * (math.sin(alpha))**2) / (2 * g)
if H >= R:
    print("Снаряд поразит цель.")
else:
    print("Снаряд не достигнет цели по высоте.")
