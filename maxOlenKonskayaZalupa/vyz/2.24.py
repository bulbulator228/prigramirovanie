x = float(input("Введите первое число: "))
y = float(input("Введите второе число: "))
s = x + y
d = x - y
p = x * y
q = x / y if y != 0 else 'Деление на 0 невозможно'
print("Сумма:", s)
print("Разность:", d)
print("Произведение:", p)
print("Частное:", q)
