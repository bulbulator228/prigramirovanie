import math
y = float(input("Введите угол y (в радианах, 0 < y ≤ 2π): "))
deg = y * 180 / math.pi
hours = int(deg // 30)  # 30° на час
remainder = deg % 30
minutes = int(remainder * 2)  # 0.5° на минуту => мин = град * 2
minute_angle = minutes * 6
print(f"Полные часы: {hours}")
print(f"Полные минуты: {minutes}")
print(f"Угол минутной стрелки: {minute_angle}°")
