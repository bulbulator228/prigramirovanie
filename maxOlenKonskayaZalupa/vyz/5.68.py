n = int(input("Введите n (2 < n ≤ 10): "))
factorial = 1
sum_factorials = 0
for k in range(1, n + 1):
    factorial *= k
    sum_factorials += factorial
print("Сумма factorials:", sum_factorials)