k = int(input("Введите k (1-180): "))
sequence = ''.join(str(i) for i in range(10, 100))
digit = sequence[k - 1]
print(f"К {k}-я цифра: {digit}")