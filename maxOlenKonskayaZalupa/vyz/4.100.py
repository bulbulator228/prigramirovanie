x, y = map(float, input("Введите два числа: ").split())
# а) два неполных условия
max_num = x if x > y else y
min_num = y if x > y else x
print("Наибольшее:", max_num)
print("Наименьшее:", min_num)
# б) один неполный условный оператор
max_num = x if x > y else y
min_num = y if x > y else x
print("Наибольшее (один оператор):", max_num)
print("Наименьшее (один оператор):", min_num)