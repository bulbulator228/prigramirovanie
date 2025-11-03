import math

# Внутренний диаметр внутреннего шара
d_inner = 10  # см
t = 0.5  # мм = 0.05 см
r_inner = d_inner / 2
r_outer = r_inner + t

# Объем шара: V = (4/3) * pi * R^3
volume_outer = (4/3) * math.pi * r_outer**3
volume_inner = (4/3) * math.pi * r_inner**3
volume_ball = volume_outer - volume_inner

# В литрах: 1 см^3 = 0.001 л
total_volume_liters = volume_ball * 0.001 * 12
print(f"Общий объем 12 шаров: {total_volume_liters:.2f} литров")