for a in range(1, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            n = c * 100 + b * 10 + a
            if n == 654:
                x = a * 100 + b * 10 + c
                print(f"x = {x}")
