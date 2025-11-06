a = int(input("Введите a: "))
b = int(input("Введите b: "))
total = sum(i for i in range(a, b + 1) if i % 4 == 0)
print(total)