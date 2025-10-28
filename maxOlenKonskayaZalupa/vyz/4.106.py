import math
a, b = map(float, input("Введите два числа: ").split())
if math.sqrt(b) < a:
    b *= 5
print("Результат второго числа:", b)
