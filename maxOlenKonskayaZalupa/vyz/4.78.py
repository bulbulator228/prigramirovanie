def same_color(a, b, c, d):
    return (a + b) % 2 == (c + d) % 2
print(same_color(1, 1, 2, 2))
print(same_color(1, 1, 2, 3))

