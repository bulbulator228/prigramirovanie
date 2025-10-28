x, y = map(float, input("Введите два числа: ").split())
# а) два неполных условия
max_num = x if x > y else y
print("Наибольшее:", max_num)
# б) один неполный условный оператор
max_num = x if x > y else y
print("Наибольшее (один оператор):", max_num)