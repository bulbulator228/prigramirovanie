a, b, c = map(float, input("Введите три числа: ").split())

# а) наибольшее
max_num = a if a > b else b
max_num = max_num if max_num > c else c

# б) наименьшее
min_num = a if a < b else b
min_num = min_num if min_num < c else c

print("Наибольшее:", max_num)
print("Наименьшее:", min_num)