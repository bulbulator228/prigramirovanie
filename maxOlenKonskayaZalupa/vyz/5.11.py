import math
for height in range(1, 11):
    distance = math.sqrt(2 * 6350 * height)
    print(f"Высота: {height} км, расстояние до горизонта: {distance:.2f} км")