n = int(input("Введите n: "))
fib = [0, 1]
for _ in range(2, n):
    fib.append(fib[-1] + fib[-2])
sum_n = sum(fib[:n])
print("Четная сумма:" , sum_n % 2 == 0)