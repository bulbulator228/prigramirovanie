import math
# а) от 7 до 14
prod1 = 1
for i in range(7, 15):
    prod1 *= i
print(f"Произведение чисел от 7 до 14: {prod1}")

# б) от a до 15
a = int(input("Введите a (1 ≤ a ≤ 15): "))
prod2 = 1
for i in range(a, 16):
    prod2 *= i
print(f"Произведение от {a} до 15: {prod2}")

# в) от 1 до b
b = int(input("Введите b (1 ≤ b ≤ 10): "))
prod3 = 1
for i in range(1, b + 1):
    prod3 *= i
print(f"Произведение от 1 до {b}: {prod3}")

# г) от a до b
a = int(input("Введите a: "))
b = int(input("Введите b (b ≥ a): "))
prod4 = 1
for i in range(a, b + 1):
    prod4 *= i
print(f"Произведение от {a} до {b}: {prod4}")