for x in range(100, 1000):
    a = x // 100
    b = (x // 10) % 10
    c = x % 10
    if c * 100 + 10 * a + b == 237:
        print("3.32 Число x =", x)
        break