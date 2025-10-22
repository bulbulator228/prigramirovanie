for a in range(1, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            if (10 * a + c) * 10 + b == 456:
                x = 100 * a + 10 * b + c
                print("3.38 Число x =", x)
                break