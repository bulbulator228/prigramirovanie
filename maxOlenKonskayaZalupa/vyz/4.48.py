x, y = map(int, input("Введите два целых числа через пробел: ").split())
result = (x != 0 and y % x == 0) or (y != 0 and x % y == 0)
print("Хотя бы одно число делитель другого:", result)
