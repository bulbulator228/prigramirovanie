n = int(input("Введите n: "))
total = 0
for k in range(1, n + 1):
    if n == 1:
        total += 1
    elif n == 2:
        total += 3 + 5
    elif n == 3:
        total += 7 + 9 + 11
    elif n == 5:
        total += 21 + 23 + 25 + 27 + 29
print(f"{n}^3 равно {total}")