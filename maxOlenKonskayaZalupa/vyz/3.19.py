num = int(input("Введите трёхзначное число: "))
a = num // 100
b = (num // 10) % 10
c = num % 10
print(f"{a}, {b}, {c}")