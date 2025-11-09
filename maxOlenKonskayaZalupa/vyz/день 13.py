# 6.1.
def integer_division(a, b):
    count = 0
    sum_b = b
    while sum_b <= a:
        sum_b += b
        count += 1
    return count

def remainder(a, b):
    quotient = integer_division(a, b)
    product = 0
    for _ in range(quotient):
        product += b
    remainder_value = a
    for _ in range(product):
        remainder_value -= 1
    return remainder_value

# Задача 6.2.
def print_numbers_upto_n(n):
    counter = 1
    while True:
        if counter > n:
            break
        print(counter)
        counter += 1

# Задача 6.3.
def print_odd_numbers():
    number = 11
    while number <= 99:
        print(number)
        number += 2

# Задача 6.4.
def find_min_divisible_over_190():
    num = 191
    while True:
        if num % 17 == 0:
            print(num)
            break
        num += 1

# Задача 6.5.
def max_divisible_by_139():
    n = 5000
    max_num = 0
    num = 139
    while num <= n:
        max_num = num
        num += 139
    print(max_num)

# Задача 6.6.
def factorial(n):
    result = 1
    current = n
    while current > 1:
        result *= current
        current -= 1
    return result

# Задача 6.7.
def print_numbers_square_upto_n(n):
    num = 1
    while True:
        if num * num > n:
            break
        print(num)
        num += 1

# Задача 6.8.
def first_number_square_greater_than_n(n):
    num = 1
    while num <= 100:
        if num * num > n:
            print(num)
            break
        num += 1


# Задача 6.9.
def input_even_number():
    while True:
        num = int(input("Введите четное число: "))
        if num % 2 == 0:
            print(f"Вы ввели четное число: {num}")
            break
        else:
            print("Ошибка: число нечетное. Попробуйте снова.")
# 6.10. Ввод пароля
password = 12345  # Установленный пароль
while True:
    try:
        user_input = int(input("Введите пароль: "))
        if user_input == password:
            print("Добро пожаловать!")
            break
        else:
            print("Ошибка: неправильный пароль. Попробуйте снова.")
    except ValueError:
        print("Ошибка: введите целое число.")

# 6.11.
numbers = []
for _ in range(10):
    num = int(input("Введите число: "))
    if num == 0:
        break
    numbers.append(num)

# 6.12.
while True:
    num = int(input("Введите число (последнее число должно быть 0): "))
    print("Вы ввели число:", num)
    if num == 0:
        break

# 6.13.

# а) с предусловием
i = 10
while i <= 30:
    print(i)
    i += 1

# б) с постусловием

i = 10
if i <= 30:
    while True:
        print(i)
        i += 1
        if i > 30:
            break

#6.14
number = 100
while number >= 80:
    print(number)
    number -= 1

#6.15
n = 21
for n in range(21, 152, 10):
    print(n, 2 * n)

#6.16
n = 2
while n <= 12:
    print(n)
    n += 0.5

#6.17
n = 1.0
while n <= 13.5:
    print(n)
    n += 0.5

#6.18
#a
import math
a = 10  # пример значений
b = 5
n = a
while n >= b:
    print(math.sqrt(n))
    n -= 1
#b
import math
a = 10
b = 5
n = a
while True:
    print(math.sqrt(n))
    n -= 1
    if n < b:
        break

#6.19
number = int(input("Введите натуральное число: "))
for digit in str(number):
    print(digit)

#6.20
number = int(input("Введите натуральное число: "))
digits = []
temp = number
while temp > 0:
    digits.append(temp % 10)
    temp //= 10
sum_digits = sum(digits)
count_digits = len(digits)
product_digits = 1
for d in digits:
    product_digits *= d
average = sum_digits / count_digits
sum_squares = sum(d ** 2 for d in digits)
sum_cubes = sum(d ** 3 for d in digits)
first_digit = int(str(number)[0])
last_digit = digits[0]
sum_first_last = first_digit + last_digit
print("Сумма цифр:", sum_digits)
print("Количество цифр:", count_digits)
print("Произведение цифр:", product_digits)
print("Среднее арифметическое:", average)
print("Сумма квадратов цифр:", sum_squares)
print("Сумма кубов цифр:", sum_cubes)
print("Первая цифра:", first_digit)
print("Сумма первой и последней цифр:", sum_first_last)

#6.21
number = int(input("Введите натуральное число (>9): "))
digits = list(str(number))
if len(digits) >= 2:
    print("Вторая цифра:", digits[1])
else:
    print("Ошибка: число менее 2 цифр.")

#6.22
number = int(input("Введите натуральное число (>99): "))
digits = list(str(number))
if len(digits) >= 3:
    print("Третья цифра:", digits[2])
else:
    print("Ошибка: число менее 3 цифр.")

#6.23
number = int(input("Введите натуральное число: "))
m = int(input("Введите m (количество последних цифр): "))
digits_str = str(number)
if len(digits_str) >= m:
    last_digits = digits_str[-m:]
    sum_m_digits = sum(int(d) for d in last_digits)
    print("Сумма последних m цифр:", sum_m_digits)
else:
    print("Число менее чем m цифр. Обработка невозможна.")

#6.24
number = str(input("Введите число: "))
digits = list(map(int, number))
length = len(digits)

# а) по формуле a0 - a1 + a2 - ... (с началом с первого)
sum_alternate_forward = 0
for i, d in enumerate(digits):
    if i % 2 == 0:
        sum_alternate_forward += d
    else:
        sum_alternate_forward -= d
print("Знакочередующаяся сумма (начиная с ||):", sum_alternate_forward)

# б) по формуле a_k - a_{k-1} + ... (с конца)
sum_alternate_backward = 0
for i in range(length -1, -1, -1):
    if (length - 1 - i) % 2 == 0:
        sum_alternate_backward += digits[i]
    else:
        sum_alternate_backward -= digits[i]
print("Обратная знакочередующаяся сумма:", sum_alternate_backward)

#6.25
n = int(input("Введите число: "))
d = 2
while d <= n:
    if n % d == 0:
        print("Наименьший делитель, отличный от 1:", d)
        break
    d += 1

#6.26
#a
print("Кратные 13 (без цикла):")
for num in range(13, 100, 13):
    print(num)

#b
num = 13
while num < 100:
    print(num)
    num += 13

# Задача 6.27
start = 100
count = 0
number = start
result = []
while count < 15:
    if number % 19 == 0:
        result.append(number)
        count += 1
    number += 1
print("Первые 15 натуральных чисел, делящихся на 19, начиная с 100:", result)

# Задача 6.28
start = 500
count = 0
number = start
result = []
while count < 20:
    if (number % 13 == 0) or (number % 17 == 0):
        result.append(number)
        count += 1
    number += 1
print("Первые 20 натуральных чисел, делящихся на 13 или 17, начиная с 500:", result)

# Задача 6.29
start = 100
count = 0
number = start
result = []
while count < 10:
    if (number % 9 == 0) and (str(number)[-1] == '7'):
        result.append(number)
        count += 1
    number += 1
print("10 первых чисел, заканчивающихся на 7, кратных 9:", result)

# Задача 6.30
a = int(input("Введите a: "))
b = int(input("Введите b: "))
# а) результат целочисленного деления b на a без использования //
quotient = 0
temp_b = b
# Пока temp_b >= a, отнимаем a и считаем, сколько раз это делается
while temp_b >= a:
    temp_b -= a
    quotient += 1
print("Результат целочисленного деления (b // a):", quotient)
# б) остаток от деления b на a
remainder = b - quotient * a
print("Остаток от деления (b % a):", remainder)

# Задача 6.31
initial = 1000
monthly_increase_pct = 0.02
target_increase = 30
target_amount = 1200
# а) месяц, когда увеличение превысит 30 рублей
current = initial
month = 1
while True:
    increment = current * monthly_increase_pct
    if increment > target_increase:
        break
    current += increment
    month += 1
print("Месяц, когда увеличение превысит 30 руб:", month)
# б) сколько месяцев потребуется, чтобы превысить 1200 руб
current = initial
months = 0
while current <= target_amount:
    current += current * monthly_increase_pct
    months += 1
print("Количество месяцев, чтобы превысить 1200 руб:", months)

# Задача 6.32
distance_day1 = 10
multiplier = 0.10

# а) день, когда пробег больше 20 км
day = 1
distance = distance_day1
while distance <= 20:
    distance += distance * multiplier
    day += 1
print("День, когда пробег впервые превысит 20 км:", day)

# б) день, когда суммарный пробег превысит 100 км
total = 0
day = 0
distance = distance_day1
while total <= 100:
    total += distance
    distance += distance * multiplier
    day += 1
print("День, когда суммарный пробег превысит 100 км:", day)

# Задача 6.33
initial_area = 100
area_increase_pct = 0.05
initial_yield = 20
yield_increase_pct = 0.02

# а) когда урожайность превысит 22
year = 1
current_area = initial_area
current_yield = initial_yield
while current_yield <= 22:
    current_area *= (1 + area_increase_pct)
    current_yield *= (1 + yield_increase_pct)
    year += 1
print("Год, когда урожайность превысит 22 ц/га:", year)

# б) когда площадь станет больше 120 га
year = 1
current_area = initial_area
current_yield = initial_yield
while current_area <= 120:
    current_area *= (1 + area_increase_pct)
    current_yield *= (1 + yield_increase_pct)
    year += 1
print("Год, когда площадь станет больше 120 га:", year)

# в) когда общий урожай превысит 800 ц
year = 1
total_yield = 0
current_area = initial_area
current_yield = initial_yield
while total_yield <= 800:
    annual_yield = current_area * current_yield
    total_yield += annual_yield
    current_area *= (1 + area_increase_pct)
    current_yield *= (1 + yield_increase_pct)
    year += 1
print("Год, когда общий урожай превысит 800 ц:", year)


# Задача 6.34

import math
m = int(input("Введите m: "))
n = int(input("Введите n: "))
a, b = m, n
while b != 0:
    a, b = b, a % b
result = []
for k in range(1, m * n + 1):
    is_multiple = ((k % m == 0) or (k % n == 0))
    if is_multiple:
        result.append(k)
print("Кратные m и n, не превышающие m*n:", result)

# Задача 6.35
number = int(input("Введите натуральное число: "))
digits_str = str(number)
# а) количество цифр 3
count_3 = digits_str.count('3')

# б) сколько раз встречается последняя цифра
last_digit = digits_str[-1]
count_last_digit = digits_str.count(last_digit)

# в) количество четных цифр
even_digits = ['0', '2', '4', '6', '8']
count_even = sum(d in even_digits for d in digits_str)

# г) сумма цифр, больших пяти
sum_greater_than_five = sum(int(d) for d in digits_str if int(d) > 5)

# д) произведение цифр, больших семи
product_greater_than_seven = 1
has_digits_greater_than_seven = False
for d in digits_str:
    digit = int(d)
    if digit > 7:
        product_greater_than_seven *= digit
        has_digits_greater_than_seven = True
if not has_digits_greater_than_seven:
    product_greater_than_seven = 0

# е) сколько раз встречаются цифры 0 и 5 (всего)
count_0 = digits_str.count('0')
count_5 = digits_str.count('5')
total_zeros_and_fives = count_0 + count_5

print("Количество цифр 3:", count_3)
print("Количество раз, когда встречается последняя цифра:", count_last_digit)
print("Количество четных цифр:", count_even)
print("Сумма цифр, больших пяти:", sum_greater_than_five)
print("Произведение цифр, больших семи:", product_greater_than_seven)
print("Всего цифр 0 и 5:", total_zeros_and_fives)

#6.36
n = int(input("Введите натуральное число: "))
str_n = str(n)
result = 0
for i in range(len(str_n)-1, -1, -1):
    if str_n[i] == '8':
        result = len(str_n) - i
        break
print(result)

#6.37
n = int(input("Введите натуральное число: "))
str_n = str(n)
result = 0
for i in range(len(str_n)-1, -1, -1):
    if str_n[i] == '8':
        result = len(str_n) - i
        break
print(result)

#6.38
n = int(input("Введите натуральное число: "))
str_n = str(n)
result = 0
for i in range(len(str_n)-1, -1, -1):
    if str_n[i] == '3':
        result = len(str_n) - i
        break
print(result)

#6.39
n = int(input("Введите натуральное число: "))
for digit in str(n):
    print(digit)

#6.40
n = int(input("Введите натуральное число: "))
str_n = str(n)
first_digit = str_n[0]
count = 0
for digit in str_n:
    if digit == first_digit:
        count += 1
print(count)

#6.41
n = int(input("Введите натуральное число: "))
max_digit = 0
min_digit = 9
for digit in str(n):
    d = int(digit)
    if d > max_digit:
        max_digit = d
    if d < min_digit:
        min_digit = d
print("Максимальная цифра:", max_digit)
print("Минимальная цифра:", min_digit)

#6.42
n = int(input("Введите натуральное число: "))
max_digit = 0
min_digit = 9
for digit in str(n):
    d = int(digit)
    if d > max_digit:
        max_digit = d
    if d < min_digit:
        min_digit = d
difference = max_digit - min_digit
sum_digits = max_digit + min_digit
print("Максимальная и минимальная цифры:", max_digit, min_digit)
print("Разница:", difference)
print("Сумма:", sum_digits)

#6.43
a = int(input("Введите число a: "))
n = int(input("Введите натуральное число: "))
max_digit = 0
min_digit = 9
for digit in str(n):
    d = int(digit)
    if d > max_digit:
        max_digit = d
    if d < min_digit:
        min_digit = d
sum_max_min = max_digit + min_digit
if sum_max_min % a == 0:
    print("Сумма максимальной и минимальной цифр кратна числу a")
else:
    print("Не делится")

#6.44
n = int(input("Введите натуральное число: "))
max_digit = 0
min_digit = 9
for digit in str(n):
    d = int(digit)
    if d > max_digit:
        max_digit = d
    if d < min_digit:
        min_digit = d
difference = max_digit - min_digit
if difference % 2 == 0:
    print("Разность четная")
else:
    print("Разность нечетная")

#6.45
n = int(input("Введите натуральное число: "))
digits = str(n)
len_n = len(digits)
max_digit = -1
min_digit = 10
pos_max = 0
pos_min = 0
for i in range(len_n):
    d = int(digits[i])
    if d > max_digit:
        max_digit = d
        pos_max = i
    if d < min_digit:
        min_digit = d
        pos_min = i
print("Позиция максимальной цифры от начала:", pos_max + 1)
print("Позиция минимальной цифры от начала:", pos_min + 1)
print("Позиция максимальной цифры от конца:", len_n - pos_max)
print("Позиция минимальной цифры от конца:", len_n - pos_min)

#6.46
n = int(input("Введите натуральное число: "))
digits = str(n)
len_n = len(digits)
max_digit = -1
min_digit = 10
pos_max = 0
pos_min = 0
for i in range(len_n):
    d = int(digits[i])
    if d > max_digit:
        max_digit = d
        pos_max = i
    if d < min_digit:
        min_digit = d
        pos_min = i
print("Позиция максимальной цифры от начала:", pos_max + 1)
print("Позиция минимальной цифры от начала:", pos_min + 1)
print("Позиция максимальной цифры от конца:", len_n - pos_max)
print("Позиция минимальной цифры от конца:", len_n - pos_min)

#6.47
n = int(input("Введите натуральное число: "))
digits = str(n)
max_digit = -1
min_digit = 10
pos_max = 0
pos_min = 0
for i in range(len(digits)):
    d = int(digits[i])
    if d > max_digit:
        max_digit = d
        pos_max = i
    if d < min_digit:
        min_digit = d
        pos_min = i
if pos_max < pos_min:
    print("Максимальная цифра расположена левее минимальной")
else:
    print("Минимальная цифра расположена левее максимальной")

#6.48
n = int(input("Введите натуральное число: "))
max_odd = -1
min_digit = 10
min_pos = 0
digits = str(n)
for i, d in enumerate(digits):
    digit_d = int(d)
    # ищем максимальную нечетную
    if digit_d % 2 == 1 and digit_d > max_odd:
        max_odd = digit_d
    # ищем минимальную цифру
    if digit_d < min_digit:
        min_digit = digit_d
        min_pos = i
if max_odd == -1:
    print("Нет нечетных цифр")
else:
    print("Максимальная нечетная цифра:", max_odd)
print("Позиция минимальной цифры слева:", min_pos + 1)

#6.49
num = input("Введите натуральное число: ")
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
k = int(input("Введите число k (для проверки k-значности): "))
m = int(input("Введите число m (для сравнения с первой цифрой): "))

# Проверка а)
sum_digits = sum(int(d) for d in num)
condition_a = sum_digits < a

# Проверка б)
prod_digits = 1
for d in num:
    prod_digits *= int(d)
condition_b = prod_digits > b

# Проверка в)
condition_v = len(num) == k

# Проверка г)
condition_g = int(num[0]) > m

print("Условие (а):", condition_a)
print("Условие (б):", condition_b)
print("Условие (в):", condition_v)
print("Условие (г):", condition_g)

#6.51
num = input("Введите натуральное число: ")
k = int(input("Введите число k: "))
b = int(input("Введите число b: "))
x = input("Введите цифру x (начальная цифра): ")
y = input("Введите цифру y (конечная цифра): ")
a = int(input("Введите число a: "))
n = int(input("Введите число n: "))

# Проверка а)
sum_digits = sum(int(d) for d in num)
condition_a = (sum_digits > k) and (int(num[-1]) % 2 == 0)

# Проверка б)
condition_b = (len(num) % 2 == 0) and (int(num) <= b)

# Проверка г)
condition_g = (num[0] == x) and (num[-1] == y)

# Проверка д)
prod_digits = 1
for d in num:
    prod_digits *= int(d)
condition_d = (prod_digits < a) and (int(num) % b == 0)

# Проверка е)
m = int(input("Введите число m: "))
condition_e = (sum_digits > m) and (int(num) % n == 0)

print("Условие (а):", condition_a)
print("Условие (б):", condition_b)
print("Условие (г):", condition_g)
print("Условие (д):", condition_d)
print("Условие (е):", condition_e)

# 6.52.
def task_6_52(number):
    s = str(number)
    has_3 = '3' in s
    has_2_and_5 = ('2' in s) and ('5' in s)
    return has_3, has_2_and_5

# 6.53.
def task_6_53(number, a, b, k):
    s = str(number)
    count_a = s.count(str(a))
    has_a = str(a) in s
    has_b = str(b) not in s
    more_k_a = count_a > k
    has_b_and_a = ('{}'.format(a) in s) and ('{}'.format(b) in s)
    return has_a, has_b, more_k_a, has_b_and_a

# 6.54.
def task_6_54(number):
    s = str(number)
    count_0 = s.count('0')
    count_9 = s.count('9')
    if count_0 > count_9:
        return '0'
    elif count_9 > count_0:
        return '9'
    else:
        return 'равное количество'

# 6.55.
def task_6_55(number, a, b):
    s = str(number)
    count_a = s.count(str(a))
    count_b = s.count(str(b))
    return count_a < count_b

# 6.56.
def task_6_56(number):
    s = str(number)
    index_2 = s.find('2')
    index_5 = s.find('5')
    if index_2 == -1 and index_5 == -1:
        return None
    if index_2 == -1:
        return '5'
    if index_5 == -1:
        return '2'
    return '2' if index_2 < index_5 else '5'

# 6.57.
def task_6_57(number, a, b):
    s = str(number)
    index_a = s.rfind(str(a))
    index_b = s.rfind(str(b))
    if index_a == -1 and index_b == -1:
        return None
    if index_a == -1:
        return str(b)
    if index_b == -1:
        return str(a)
    return str(a) if index_a > index_b else str(b)

# 6.58.
def task_6_58(number):
    s = str(number)
    max_digit = max(s)
    count = 0
    # Два цикла
    for ch in s:
        if ch == max_digit:
            count += 1
    return count

def task_6_58_single_loop(number):
    s = str(number)
    max_digit = '0'
    count_max = 0
    for ch in s:
        if ch > max_digit:
            max_digit = ch
            count_max = 1
        elif ch == max_digit:
            count_max += 1
    return count_max

# 6.59.
def task_6_59(number):
    s = str(number)
    min_digit = min(s)
    count = 0
    # Два цикла
    for ch in s:
        if ch == min_digit:
            count += 1
    return count

def task_6_59_single_loop(number):
    s = str(number)
    min_digit = '9'
    count_min = 0
    for ch in s:
        if ch < min_digit:
            min_digit = ch
            count_min = 1
        elif ch == min_digit:
            count_min += 1
    return count_min

#6.60
number = int(input("Введите натуральное число с различными цифрами: "))
max_digit = 0
min_digit = 9

for digit in str(number):
    d = int(digit)
    if d > max_digit:
        max_digit = d
    if d < min_digit:
        min_digit = d

print(f"Максимальная цифра: {max_digit}")
print(f"Минимальная цифра: {min_digit}")

#6.61
number = int(input("Введите натуральное число с различными цифрами: "))
digits = [int(d) for d in str(number)]
length = len(digits)
max_digit = max(digits)
min_digit = min(digits)
max_positions_from_start = [i + 1 for i, d in enumerate(digits) if d == max_digit]
max_positions_from_end = [length - i for i, d in enumerate(digits) if d == max_digit]
min_positions_from_start = [i + 1 for i, d in enumerate(digits) if d == min_digit]
min_positions_from_end = [length - i for i, d in enumerate(digits) if d == min_digit]
print(f"Позиции двух максимальных цифр (от начала): {max_positions_from_start[:2]}")
print(f"Позиции двух максимальных цифр (от конца): {max_positions_from_end[:2]}")
print(f"Позиции двух минимальных цифр (от начала): {min_positions_from_start[:2]}")
print(f"Позиции двух минимальных цифр (от конца): {min_positions_from_end[:2]}")

#6.62
number = input("Введите натуральное число: ")

# а)
reversed_number = number[::-1]

# б)
doubled_number = '22' + number + '22'

# в)
a = input("Введите цифру для удаления: ")
removed_a = ''.join(d for d in number if d != a)

# г)
if len(number) > 1:
    permuted_number = number[-1] + number[1:-1] + number[0]
else:
    permuted_number = number

# д)
doubled = number * 2

print(f"Обратное число: {reversed_number}")
print(f"Приписывание по две цифры: {doubled_number}")
print(f"Удаление цифр {a}: {removed_a}")
print(f"Перестановка первой и последней цифр: {permuted_number}")
print(f"Образование числа путем приписывания: {doubled}")

#6.63
number = input("Введите натуральное число: ")
if number == number[::-1]:
    print("Является палиндромом")
else:
    print("Не является палиндромом")

#6.64
n = int(input("Введите сумму: "))
denominations = [64, 32, 16, 8, 4, 2, 1]
counts = []
for d in denominations:
    count = n // d
    counts.append((d, count))
    n %= d
print("Используемые купюры:")
for denom, count in counts:
    print(f"{denom} - {count}")

#6.65
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
while b != 0:
    a, b = b, a % b
print(f"Наибольший общий делитель: {a}")

#6.66
def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))
gcd_ab = gcd(a, b)
gcd_abc = gcd(gcd_ab, c)
print(f"Наибольший общий делитель трёх чисел: {gcd_abc}")

#6.67
a = int(input("Введите числитель: "))
b = int(input("Введите знаменатель: "))
def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x
div = gcd(a, b)
p = a // div
q = b // div
print(f"Сокращенная дробь: {p}/{q}")

#6.68
width = 425
height = 131
squares = []
while width >= height and height > 0:
    count = width // height
    squares.append((height, count))
    width, height = height, width % height
print("Квадраты и их количество:")
for side, count in squares:
    print(f"Со стороной {side} - {count} шт")

#6.69
def rectangle_squares(length, width):
    squares = {}
    while length != 0 and width != 0:
        if length >= width:
            count = length // width
            squares[width] = squares.get(width, 0) + count
            length = length % width
        else:
            count = width // length
            squares[length] = squares.get(length, 0) + count
            width = width % length
    return squares
# Пример для 425×131
result = rectangle_squares(425, 131)
print("Квадраты размере:")
for side, quantity in result.items():
    print(f"{side} — {quantity} раз(а)")

#6.70
def rectangle_squares_general(a, b):
    squares = {}
    while a != 0 and b != 0:
        if a >= b:
            count = a // b
            squares[b] = squares.get(b, 0) + count
            a = a % b
        else:
            count = b // a
            squares[a] = squares.get(a, 0) + count
            b = b % a
    return squares
a, b = 520, 312  # Можно изменить размеры
result = rectangle_squares_general(a, b)
print("Квадраты размере:")
for side, quantity in result.items():
    print(f"{side} — {quantity} раз(а)")

#6.71
import math
def is_fibonacci(n):
    if n < 0:
        return False
    # проверка через тест (5*n^2 + 4) или (5*n^2 - 4)
    return any([
        int(math.sqrt(5 * n * n + 4))**2 == 5 * n * n + 4,
        int(math.sqrt(5 * n * n - 4))**2 == 5 * n * n - 4
    ])
num = int(input("Введите число: "))
print(f"{num} является членом последовательности Фибоначчи" if is_fibonacci(num) else f"{num} не является членом последовательности Фибоначчи")

#6.72
def is_arith_progression(n, f, s):
    if s == 0:
        return n == f  # Если шаг 0, то число должно быть равно первому члену
    return (n - f) % s == 0 and (n - f) // s >= 0
n = int(input("Введите число: "))
f = int(input("Первый член прогрессии: "))
s = int(input("Шаг: "))
print(f"Число {n} входит в арифметическую прогрессию" if is_arith_progression(n, f, s) else f"Число {n} не входит в арифметическую прогрессию")

#6.73
def is_geo_progression(m, g, z):
    if g == 0:
        return m == 0
    if z == 0:
        return False
    if m == g:
        return True
    if (m % g != 0):
        return False
    ratio = m // g
    return ratio == z ** (int(math.log(ratio, z)))
m = int(input("Введите число: "))
g = int(input("Первый член прогрессии: "))
z = int(input("Знаменатель: "))
print(f"Число {m} входит в геометрическую прогрессию" if is_geo_progression(m, g, z) else f"Число {m} не входит в геометрическую прогрессию")

#6.74
def is_power_of(base, num):
    if num < 1:
        return False
    while num != 1:
        if num % base != 0:
            return False
        num //= base
    return True
n = int(input("Введите число: "))
print(f"{n} является степенью 3" if is_power_of(3, n) else f"{n} не является степенью 3")
print(f"{n} является степенью 5" if is_power_of(5, n) else f"{n} не является степенью 5")

#6.75
def bisection_method(f, a, b, epsilon=0.001):
    while abs(b - a) > epsilon:
        c = (a + b) / 2
        if f(c) * f(a) <= 0:
            b = c
        else:
            a = c
    return (a + b) / 2
# a)
def f1(x):
    return x**4 + 2*x**3 - x - 1
root1 = bisection_method(f1, 0, 1)
print(f"Приближенное значение корня для первой функции: {root1:.3f}")

# б)
def f2(x):
    return x**3 - 0.2*x**2 - 0.2*x - 1.2
root2 = bisection_method(f2, 1, 1.5)
print(f"Приближенное значение корня для второй функции: {root2:.3f}")

#6.76
def spiral_length(a, b):
    length = 0
    min_dim, max_dim = a, b
    while min_dim > 1 and max_dim > 1:
        perimeter = 2 * (min_dim + max_dim - 2)
        length += perimeter
        min_dim -= 2
        max_dim -= 2
    return length
# пример: для 4x6
a, b = 4, 6
print(f"Длина ограждения = {spiral_length(a, b)}")

#6.77
def all_digits_same(n):
    s = str(n)
    return all(d == s[0] for d in s)
def contains_adjacent_same(n):
    s = str(n)
    return any(s[i] == s[i+1] for i in range(len(s)-1))
number = int(input("Введите натуральное число: "))
print(f"Заданное число состоит из одинаковых цифр" if all_digits_same(number) else "Заданное число не состоит из одинаковых цифр")
print(f"Заданное число содержит две одинаковые цифры подряд" if contains_adjacent_same(number) else "Заданное число не содержит двух одинаковых цифр подряд")

#6.78
num = int(input("Введите натуральное число: "))
prev_digit = 10
is_sorted = True
while num > 0:
    digit = num % 10
    if digit > prev_digit:
        is_sorted = False
        break
    prev_digit = digit
    num //= 10
print("Последовательность цифр справа налево упорядочена по возрастанию:" , is_sorted)

#6.79
num = int(input("Введите натуральное число: "))
prev_digit = 0
is_non_decreasing = True
while num > 0:
    digit = num % 10
    if digit < prev_digit:
        is_non_decreasing = False
        break
    prev_digit = digit
    num //= 10
print("Последовательность справа налево упорядочена по неубыванию:" , is_non_decreasing)

#6.80
num = int(input("Введите натуральное число: "))
prev_digit = -1
is_increasing = True
while num > 0:
    digit = num % 10
    if digit < prev_digit:
        is_increasing = False
        break
    prev_digit = digit
    num //= 10
print("Последовательность слева направо упорядочена по возрастанию:" , is_increasing)

#6.81
num = int(input("Введите число: "))
prev_digit = -1
is_mono_increasing = True
while num > 0:
    digit = num % 10
    if prev_digit != -1 and digit <= prev_digit:
        is_mono_increasing = False
        break
    prev_digit = digit
    num //= 10
print("Цифры слева направо образуют монотонно возрастающую последовательность:" , is_mono_increasing)

#6.82
num = int(input("Введите натуральное число: "))
prev_digit = 0
is_non_decreasing = True
while num > 0:
    digit = num % 10
    if digit < prev_digit:
        is_non_decreasing = False
        break
    prev_digit = digit
    num //= 10
print("Цифры слева направо упорядочены по неубыванию:" , is_non_decreasing)

#6.83
num = int(input("Введите число: "))
prev_digit = -1
is_mono_increasing = True
is_mono_decreasing = True
while num > 0:
    digit = num % 10
    if prev_digit != -1:
        if digit <= prev_digit:
            is_mono_increasing = False
        if digit >= prev_digit:
            is_mono_decreasing = False
    prev_digit = digit
    num //= 10
print("Монотонно возрастающая или убывающая последовательность:" , (is_mono_increasing or is_mono_decreasing))

#7.1
a = [float(input(f"Введите число {i+1}: ")) for i in range(10)]
print("Сумма чисел:", sum(a))

#7.2
n = int(input("Введите количество чисел: "))
numbers = [float(input(f"Введите число {i+1}: ")) for i in range(min(10, n))]
print("Сумма всех чисел:", sum(numbers))

#7.3
sides = [float(input(f"Введите длину стороны {i+1}: ")) for i in range(12)]
perimeter = sum(sides)
print("Периметр 12-угольника:", perimeter)

#7.4
mass = [float(input(f"Масса предмета {i+1}: ")) for i in range(int(input("Количество предметов: ")))]
total_weight = sum(mass)
print("Общая масса груза:", total_weight)

#7.5
n = int(input("Количество сотрудников: "))
salaries = [float(input(f"Зарплата сотрудника {i+1}: ")) for i in range(n)]
total_salary = sum(salaries)
print("Общая сумма зарплат:", total_salary)

#7.6
resistances = [float(input(f"Сопротивление элемента {i+1}: ")) for i in range(int(input("Количество элементов: ")))]
total_resistance = sum(resistances)
print("Общее сопротивление цепи:", total_resistance)

# Задача 7.7
def parallel_resistance(resistances):
    reciprocals_sum = 0
    for r in resistances:
        reciprocals_sum += 1 / r
    return 1 / reciprocals_sum

resistances = [100, 200, 300]
print("Общее сопротивление:", parallel_resistance(resistances))

# Задача 7.8
def sum_and_count_sequence():
    total_sum = 0
    count = 0
    while True:
        num = int(input("Введите число (0 для завершения): "))
        if num == 0:
            break
        total_sum += num
        count += 1
    print("Сумма:", total_sum)
    print("Количество чисел:", count)

# Задача 7.9
def sum_of_grades():
    print("Введите оценки первого ученика:")
    student1 = [int(input(f"Оценка предмета {i + 1}: ")) for i in range(4)]
    print("Введите оценки второго ученика:")
    student2 = [int(input(f"Оценка предмета {i + 1}: ")) for i in range(4)]
    print("Сумма оценок первого ученика:", sum(student1))
    print("Сумма оценок второго ученика:", sum(student2))


# Задача 7.10
def sum_scores():
    print("Баллы первого спортсмена:")
    athlete1 = [float(input(f"Вид спорта {i + 1}: ")) for i in range(5)]
    print("Баллы второго спортсмена:")
    athlete2 = [float(input(f"Вид спорта {i + 1}: ")) for i in range(5)]
    print("Общая сумма баллов первого спортсмена:", sum(athlete1))
    print("Общая сумма баллов второго спортсмена:", sum(athlete2))


# Задача 7.11
def product_of_numbers():
    nums = [float(input(f"Введите число {i + 1}: ")) for i in range(8)]
    product = 1
    for num in nums:
        product *= num
    print("Произведение:", product)


# Задача 7.12
def output_subproducts():
    a1 = int(input("Введите a1: "))
    print(a1)
    product = a1
    while True:
        a_next = int(input("Введите следующее число (0 для завершения): "))
        if a_next == 0:
            break
        product *= a_next
        print(product)


# Задача 7.13
def sum_squares():
    nums = [int(input(f"a{i + 1}: ")) for i in range(10)]
    total = sum([x ** 2 for x in nums])
    print("Сумма квадратов:", total)


# Задача 7.14
def sum_squares_real():
    n = int(input("Введите n: "))
    nums = [float(input(f"a{i + 1}: ")) for i in range(n)]
    total = sum([x ** 2 for x in nums])
    print("Сумма квадратов:", total)


# Задача 7.15
def check_sum():
    nums = [float(input(f"a{i + 1}: ")) for i in range(10)]
    if sum(nums) > 100.78:
        print("Да, сумма превосходит 100.78")
    else:
        print("Нет, сумма не превосходит 100.78")


# Задача 7.16
def check_sum_b():
    n = int(input("Введите n: "))
    b = [int(input(f"b{i + 1}: ")) for i in range(10)]
    p = int(input("Введите p: "))
    total = sum(b)
    if total < p:
        print("Сумма bi меньше p")
    else:
        print("Сумма bi не меньше p")


# Задача 7.17
def check_even_sum():
    a = [int(input(f"a{i + 1}: ")) for i in range(9)]
    total = sum(a)
    if total % 2 == 0:
        print("Сумма четная")
    else:
        print("Сумма нечетная")
