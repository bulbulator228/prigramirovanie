import math
length = 4.5
distance = 3.0
for s in [i * 0.2 for i in range(int(distance / 0.2) + 1)]:
    h = math.sqrt(length**2 - s**2)
    angle_rad = math.acos(h / length)
    angle_deg = math.degrees(angle_rad)
    print(f"Расстояние от стены: {s:.2f} м, угол: {angle_deg:.2f} градусов")