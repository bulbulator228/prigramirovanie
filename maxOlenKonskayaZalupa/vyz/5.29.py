# а) от 1 до 750
sum_all = sum(range(1, 751))
average1 = sum_all / 750
print(f"Среднее от 1 до 750: {average1}")

# б) от 150 до b
b = int(input("Введите b (≥ 150): "))
count_b = b - 150 + 1
sum_b = sum(range(150, b + 1))
average2 = sum_b / count_b
print(f"Среднее от 150 до {b}: {average2}")

# в) от a до 200
a = int(input("Введите a (≤ 200): "))
count_a = 200 - a + 1
sum_a = sum(range(a, 201))
average3 = sum_a / count_a
print(f"Среднее от {a} до 200: {average3}")

# г) от a до b
a = int(input("Введите a: "))
b = int(input("Введите b (b ≥ a): "))
count_ab = b - a + 1
sum_ab = sum(range(a, b + 1))
average4 = sum_ab / count_ab
print(f"Среднее от {a} до {b}: {average4}")