n = int(input("Введите число n (1 ≤ n ≤ 999): "))
for x in range(100, 1000):
    a = x // 100
    bc = x % 100
    if bc * 10 + a == n:
        print("3.35 Число x =", x)
        break