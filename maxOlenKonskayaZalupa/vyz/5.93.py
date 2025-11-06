n = int(input("Введите число: "))
divs = [d for d in range(1, n) if n % d == 0]
if sum(divs) == n:
    print("Число совершенное")
else:
    print("Число не совершенное")