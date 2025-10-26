def triangle_exists(a, b, c):
    pass
def triangle_type(a, b, c):
    if not triangle_exists(a, b, c):
        return "Треугольник не существует"
    sides = sorted([a, b, c])
    a, b, c = sides
    c2 = c ** 2
    sum_sq = a ** 2 + b ** 2
    if abs(sum_sq - c2) < 1e-9:
        kind = "прямоугольный"
    elif sum_sq > c2:
        kind = "остроугольный"
    else:
        kind = "тупоугольный"
    if a == b == c:
        feature = "равносторонний"
    elif a == b or b == c:
        feature = "равнобедренный"
    else:
        feature = "разносторонний"
    return f"{kind}, {feature}"
print(triangle_type(3, 4, 5))
