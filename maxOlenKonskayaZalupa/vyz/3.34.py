for x in range(100, 1000):
    a = x // 100
    bc = x % 100
    if bc * 10 + a == 564:
        print("3.34 Число x =", x)
        break