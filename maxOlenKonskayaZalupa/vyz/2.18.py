import math
x = float(input('Введите симло x:'))
y = float(input('Введите симло y:'))
z = x + (2 + y) / x**2 / (y + 1 / math.sqrt(x**2 + 10))
q = 7.25 * math.sin(x) - abs(y**2)
print(z)
print(q)