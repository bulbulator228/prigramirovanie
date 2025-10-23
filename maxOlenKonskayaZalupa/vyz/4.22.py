m = float(input('Введите число m:'))
n = float(input('Введите число n:'))
if n == 0:
    print("Деление на ноль невозможно")
elif m % n == 0:
    print(f"Частное от деления: {m // n}")
else:
    print(f"{m} на {n} нацело не делится")