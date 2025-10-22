n = int(input("Введите число n (10 ≤ n ≤ 999, и число десятков в n ≠ 0): "))
found = False
for a in range(1, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            if (b * 100 + 10 * a + c == n) and ((n // 10) % 10 != 0):
                x = 100 * a + 10 * b + c
                print("3.37 Число x =", x)
                found = True
                break
    if found:
        break