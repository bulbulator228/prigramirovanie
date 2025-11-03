# а) от 200 до 600
sum1 = sum(range(200, 601))
print(f"Сумма чисел от 200 до 600: {sum1}")

# б) от a до 400
a = int(input("Введите a (≤ 400): "))
sum2 = sum(range(a, 401))
print(f"Сумма чисел от {a} до 400: {sum2}")

# в) от -15 до b
b = int(input("Введите b (≥ -15): "))
sum3 = sum(range(-15, b + 1))
print(f"Сумма чисел от -15 до {b}: {sum3}")

# г) от a до b
a = int(input("Введите a: "))
b = int(input("Введите b (≥ a): "))
sum4 = sum(range(a, b + 1))
print(f"Сумма чисел от {a} до {b}: {sum4}")