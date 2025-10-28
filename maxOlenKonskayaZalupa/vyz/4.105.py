a, b = map(float, input("Введите два числа: ").split())
abs_a = a if a >= 0 else -a
abs_b = b if b >= 0 else -b
if abs_a > abs_b:
    a /= 2
print("Результат:", a)