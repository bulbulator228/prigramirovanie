import math
x = float(input("Введите x: "))
y = float(input("Введите y: "))
abs_x = abs(x)
abs_y = abs(y)
arit = (x + y) / 2
geomet = math.sqrt(abs_x * abs_y)
print("Среднее арифметическое модулей:", arit)
print("Среднее геометрическое модулей:", geomet)
