n = int(input("Введите n (1-32): "))
sequence = ''.join(str(i) for i in range(21))
digit = sequence[n - 1]
print(f"Цифра с номером {n}: {digit}")