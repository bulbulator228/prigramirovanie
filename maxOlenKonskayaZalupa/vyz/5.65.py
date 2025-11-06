n = int(input("Введите натуральное число n: "))
sum_ = 0
for i in range(1, 2*n, 2):
    sum_ += i
print(f"{n}^2 =", sum_)