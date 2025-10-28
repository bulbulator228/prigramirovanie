a, b, c, d = map(float, input("Введите четыре числа: ").split())

# а) наибольшее

max_num = a if a > b else b
max_num = max_num if max_num > c else c
max_num = max_num if max_num > d else d

# б) наименьшее

min_num = a if a < b else b
min_num = min_num if min_num < c else c
min_num = min_num if min_num < d else d
print("Наибольшее:", max_num)
print("Наименьшее:", min_num)