import math
a = float(input("Введите основание a: "))
b = float(input("Введите основание b: "))
h = float(input("Введите высоту: "))
c = math.sqrt(h**2 + ((a - b)/2)**2)
P = a + b + 2 * c
print("Периметр трапеции:", P)