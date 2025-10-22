n = int(input("Введите число n: "))
for x in range(100, 1000):
    a = x // 100
    b = (x // 10) % 10
    c = x % 10
    if c * 100 + 10 * a + b == n:
        print("3.33 Число x =", x)
        break