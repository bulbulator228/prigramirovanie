a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

if a > b and a > c:
    max_num = a
    max_pos = "первое"
elif b > a and b > c:
    max_num = b
    max_pos = "второе"
else:
    max_num = c
    max_pos = "третье"
if a < b and a < c:
    min_num = a
    min_pos = "первое"
elif b < a and b < c:
    min_num = b
    min_pos = "второе"
else:
    min_num = c
    min_pos = "третье"
numbers = [a, b, c]
numbers_sorted = sorted(numbers)
middle = numbers_sorted[1]
if middle == a:
    middle_pos = "первое"
elif middle == b:
    middle_pos = "второе"
else:
    middle_pos = "третье"
print(f"Самое большое число: {max_num} (позиция: {max_pos})")
print(f"Самое маленькое число: {min_num} (позиция: {min_pos})")
print(f"Среднее число: {middle} (позиция: {middle_pos})")