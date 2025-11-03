# Ввод данных
n = int(input("Введите целое число n: "))
a = float(input("Введите вещественное число a: "))
result = 0.0
for _ in range(abs(n)):
    result += a
if n < 0:
    result = -result
print("Произведение:", result)