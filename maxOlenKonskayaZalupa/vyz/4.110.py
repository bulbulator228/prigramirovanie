a, b, c, d = map(float, input("Введите четыре числа: ").split())
count_neg = 0
if a < 0:
    count_neg += 1
if b < 0:
    count_neg += 1
if c < 0:
    count_neg += 1
if d < 0:
    count_neg += 1
print("Количество отрицательных:", count_neg)