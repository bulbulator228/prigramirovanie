a, b, c = map(float, input("Введите ребра кирпича a, b, c: ").split())
x, y = map(float, input("Введите стороны отверстия x, y: ").split())
edges = sorted([a, b, c])
hole = sorted([x, y])
if (edges[0] <= hole[0] and edges[1] <= hole[1]):
    print("Кирпич пройдет в отверстие")
else:
    print("Кирпич не пройдет в отверстие")
