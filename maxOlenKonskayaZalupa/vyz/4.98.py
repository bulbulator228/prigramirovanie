k = int(input("Введите k (1-222): "))
sequence = ''.join(str(i) for i in range(1, 111))
digit = sequence[k - 1]
print(f"К {k}-я цифра: {digit}")