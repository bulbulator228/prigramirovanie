a, b = map(float, input("Введите размеры конверта (a b) в мм: ").split())
c, d = map(float, input("Введите размеры открытки (c d) в мм: ").split())
if (c + 2 <= a and d + 2 <= b) or (d + 2 <= a and c + 2 <= b):
    print("Открытка войдет в конверт")
else:
    print("Открытка не войдет в конверт")
