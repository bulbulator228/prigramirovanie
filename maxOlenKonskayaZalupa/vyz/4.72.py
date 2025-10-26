x1 = float(input("Введите x-координату левого нижнего угла первого прямоугольника: "))
y1 = float(input("Введите y-координату левого нижнего угла первого прямоугольника: "))
w1 = float(input("Введите ширину первого прямоугольника: "))
h1 = float(input("Введите высоту первого прямоугольника: "))
x2 = float(input("Введите x-координату левого нижнего угла второго прямоугольника: "))
y2 = float(input("Введите y-координату левого нижнего угла второго прямоугольника: "))
w2 = float(input("Введите ширину второго прямоугольника: "))
h2 = float(input("Введите высоту второго прямоугольника: "))
def is_first_in_second():
    return (x1 >= x2) and (y1 >= y2) and (x1 + w1 <= x2 + w2) and (y1 + h1 <= y2 + h2)
def is_one_in_another():
    return is_first_in_second() or ((x2 >= x1) and (y2 >= y1) and (x2 + w2 <= x1 + w1) and (y2 + h2 <= y1 + h1))
def is_intersect():
    if x1 + w1 < x2 or x2 + w2 < x1:
        return False
    if y1 + h1 < y2 or y2 + h2 < y1:
        return False
    return True
print("\nРезультаты:")
print("а) Все точки первого прямоугольника принадлежат второму:", "Да" if is_first_in_second() else "Нет")
print("б) Все точки одного из прямоугольников принадлежат другому:", "Да" if is_one_in_another() else "Нет")
print("в) Пересекаются ли прямоугольники:", "Да" if is_intersect() else "Нет")
