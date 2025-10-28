k = int(input("Введите k (1-252): "))
sequence = ''.join(str(i) for i in range(50, 251))
digit = sequence[k - 1]
print(f"К {k}-я цифра: {digit}")