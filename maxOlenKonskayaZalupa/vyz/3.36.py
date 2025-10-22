for a in range(1, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            if b * 100 + 10 * a + c == 546:
                x = 100 * a + 10 * b + c
                print("3.36 Число x =", x)
                break