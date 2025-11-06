#1
x = int(input("Введите x: "))
y = int(input("Введите y: "))
result = 0
for _ in range(y):
    result += x
print("Произведение (через цикл):", result)

#2
def multiply(a, b):
    if b == 0:
        return 0
    else:
        return a + multiply(a, b - 1)

x = int(input("Введите x: "))
y = int(input("Введите y: "))
print("Произведение (рекурсия):", multiply(x, y))