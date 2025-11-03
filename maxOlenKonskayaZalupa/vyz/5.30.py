# а) от 25 до 40
sum_squares_a = sum(i ** 2 for i in range(25, 41))
print(f"Сумма квадратов от 25 до 40: {sum_squares_a}")

# б) от a до 50
a = int(input("Введите a (0 ≤ a ≤ 50): "))
sum_squares_b = sum(i ** 2 for i in range(a, 51))
print(f"Сумма квадратов от {a} до 50: {sum_squares_b}")

# в) от 1 до n
n = int(input("Введите n (1 ≤ n ≤ 100): "))
sum_squares_c = sum(i ** 2 for i in range(1, n + 1))
print(f"Сумма квадратов от 1 до {n}: {sum_squares_c}")

# г) от a до b
a = int(input("Введите a: "))
b = int(input("Введите b (b ≥ a): "))
sum_squares_d = sum(i ** 2 for i in range(a, b + 1))
print(f"Сумма квадратов от {a} до {b}: {sum_squares_d}")