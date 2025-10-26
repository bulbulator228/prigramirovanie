a, b, c = map(float, input("Введите стороны треугольника a, b, c: ").split())
print("Равносторонний:", a == b == c)
print("Равнобедренный:", a == b or b == c or a == c)
