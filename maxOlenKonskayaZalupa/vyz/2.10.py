x = float(input("Введите первое число: "))
y = float(input("Введите второе число: "))
arithmetic_mean = (x + y) / 2
geometric_mean = (x * y) if x > 0 and y > 0 else "Не определяется"
print("Среднее арифметическое:", arithmetic_mean)
print("Среднее геометрическое:", geometric_mean)