#7.174
scores = list(map(int, input("Введите очки 12 команд через пробел: ").split()))
top_three = sorted(scores, reverse=True)[:3]
print("Очки команд, занявших первое, второе и третье места:", top_three)

#7.175
n = int(input("Введите количество спортсменов (≥4): "))
results = list(map(int, input(f"Введите результаты {n} спортсменов в сотых долях секунды через пробел: ").split()))
best_results = sorted(results)[:4]
indices = sorted(range(len(results)), key=lambda k: results[k])[:4]
print("Индексы лучших бегунов (от 1):", [i+1 for i in indices])

#7.176
temperatures = list(map(float, input("Введите температуры за каждый день июля: ").split()))
first_min = min(temperatures)
temperatures_copy = temperatures.copy()
temperatures_copy.remove(first_min)
second_min = min(temperatures_copy)
day1 = temperatures.index(first_min) + 1
day2 = temperatures.index(second_min) + 1
print("Два самых прохладных дня:", day1, "и", day2)

#7.177
sequence = [8, 8, 8, 8]
A_values = [0, 8]
for A in A_values:
    new_sequence = sequence + [A]
    max_elements = max(new_sequence)
    count_max = new_sequence.count(max_elements)
    print(f"При A = {A}, максимальных элементов стало: {count_max}")

#7.178
numbers = list(map(int, input("Введите 12 чисел через пробел: ").split()))
max_value = max(numbers)
min_value = min(numbers)
count_max = numbers.count(max_value)
count_min = numbers.count(min_value)
print("Количество встречающихся максимумов:", count_max)
print("Количество встречающихся минимумов:", count_min)

#7.179
residents = list(map(int, input("Введите число жильцов в квартирах 1-12: ").split()))
max_residents = max(residents)
apartment_number = residents.index(max_residents) + 1
print("Квартира с наибольшим числом жильцов:", apartment_number)

#7.180
temperatures = list(map(float, input("Введите температуры за месяц: ").split()))
min_temp = min(temperatures)
days = [i+1 for i, temp in enumerate(temperatures) if temp == min_temp]
print("Количество дней с минимальной температурой:", len(days))

#7.181
sequence = list(map(int, input("Введите 20 чисел (от 0 до 66): ").split()))

# а
def is_valid_right_side(seq):
    return all((num % 10) == (num // 10) for num in seq)

# б
def is_valid_any_side(seq):
    for num in seq:
        left = num // 10
        right = num % 10
        if abs(left - right) != 1 and left != right:
            return False
    return True
print("Последовательность соответствует ряду домино (по правой стороне):", is_valid_right_side(sequence))
print("Последовательность соответствует ряду домино (по любой стороне):", is_valid_any_side(sequence))

#8.1
n = int(input("Введите n: "))
i = 1
while i * i <= n:
    print(i * i)
    i += 1

#8.2

#a
n = int(input("Введите n: "))
i = 1
while i * i <= n:
    i += 1
print(i * i)

#b
import math
n = int(input("Введите n: "))
i = int(math.sqrt(n)) + 1
print(i * i)

#8.3
a = float(input("Введите a (0 < a ≤ 1): "))
i = 1
while 1 / i >= a:
    print(1 / i)
    i += 1

#8.4
a = float(input("Введите a (0 < a ≤ 1): "))
i = 1
while 1 / i >= a:
    i += 1
print(f"Первое число из последовательности, меньше {a}:", 1 / i)

#8.5
a = float(input("Введите a (1 < a ≤ 1.5): "))
i = 1
while True:
    val = 1 + 1 / i
    if val < a:
        break
    print(val)
    i += 1

#8.6
a = float(input("Введите a (1 < a ≤ 1.5): "))
n = 1
while True:
    val = 1 + 1 / n
    if val < a:
        break
    print(val)
    n += 1

#8.7
a = float(input("Введите a (1 < a ≤ 1.5): "))
n = 1
while True:
    val = 1 + 1 / n
    if val < a:
        print(f"Первое число последовательности меньше {a}: {val}")
        break
    n += 1

#8.8
a = float(input("Введите a (1 < a ≤ 1.5): "))
max_n = int(1 / (a - 1))
print(f"Все n от 1 до {max_n}, при которых числа последовательности ≥ {a}:")
for n in range(1, max_n + 1):
    print(n)

#8.9
import math
a = float(input("Введите a (1 < a ≤ 1.5): "))
n = math.ceil(1 / (a - 1))  # наименьшее целое n, большее 1/(a-1)
print(f"Наименьшее n, при котором 1+1/n < {a}: {n}")

#8.10
a = float(input("Введите a: "))
n = 0
while True:
    if n == 0:
        val = 1
    else:
        val = 1 + 1 / n
    if val >= a:
        break
    print(val)
    n += 1

#8.11
n = int(input("Введите число n: "))
i = 0
while True:
    if i == 0:
        val = 1
    else:
        val = 1 + 1 / i
    if val > n:
        print(f"Первое число последовательности, большее {n}: {val}")
        break
    i += 1

#8.12
a = float(input("Введите a: "))
sum_harm = 0.0
for n in range(1, 100000):  # достаточно большой диапазон
    sum_harm += 1 / n
    if sum_harm > a:
        print(n)

#8.13
a = float(input("Введите a: "))
sum_harm = 0.0
n = 0
while sum_harm <= a:
    n += 1
    sum_harm += 1 / n
print(f"Наименьшее n: {n}")

#8.14
a = float(input("Введите a (0 < a ≤ 1): "))
sum_harm = 0.0
n = 0
while True:
    n += 1
    sum_harm += 1 / n
    if sum_harm < a:
        print(f"Первое число суммы, меньше а={a}: {sum_harm} при n={n}")
        break
    if sum_harm >= a:
        print(f"Нет чисел суммы меньше {a} (минимум: {sum_harm} при n={n})")
        break

#8.15
m = float(input("Введите m (0.52 ≤ m ≤ 33.7): "))
for x in range(1, 101):
    y = x**2 / 100  # пример закона
    if y < m:
        print(f"x={x}, y={y}")

#8.15 b
m = float(input("Введите m (0.52 ≤ m ≤ 33.7): "))
x = 1
while x <= 100:
    y = x**2 / 100
    if y < m:
        print(f"x={x}, y={y}")
    x += 1

#8.16
m = float(input("Введите m (0.5 < m < 1): "))
sequence = [...]  # список значений
for val in sequence:
    if val < m:
        print(val)

#8.17
num = [1, 2]  # числители
den = [1, 1]  # знаменатели
i = 2
while True:
    num.append(num[i-1] + num[i-2])
    den.append(den[i-1] + den[i-2])
    val_current = num[i] / den[i]
    val_prev = num[i-1] / den[i-1]
    if abs(val_current - val_prev) <= 0.001:
        print(f"Первый член с разницей ≤ 0.001: {val_current}")
        break
    i += 1

#8.18
a = float(input("Введите a: "))
x = float(input("Введите x: "))
epsilon = float(input("Введите ε: "))
y_prev = a
i = 2
while True:
    if y_prev == 1:
        print("Ошибка: деление на нуль в формуле!")
        break
    y_curr = 0.5 * (y_prev + x / (y_prev - 1))
    if abs(y_curr**2 - y_prev**2) < epsilon:
        print(f"Искомый член y_{i} = {y_curr}")
        break
    y_prev = y_curr
    i += 1

#8.19 a
fib = [1, 1]
s = 2
while True:
    next_fib = fib[-1] + fib[-2]
    if next_fib > 1000:
        break
    fib.append(next_fib)
    s += next_fib
print("Сумма чисел Фибоначчи ≤ 1000:", s)

#8.19 b
n = int(input("Введите n (n>1): "))
fib = [1, 1]
while True:
    next_fib = fib[-1] + fib[-2]
    if next_fib > n:
        print(f"Первое число Фибоначчи > {n}: {next_fib}")
        break
    fib.append(next_fib)

#9.1
#a
for _ in range(5):
    print("8 8 8")
#b
for i in range(1, 8):
    print((str(i) + " ") * 5)

#v
for i in range(1, 9):
    print(((str(10*i) + " ") * 4).strip())

#g

for i in range(1, 9):
    print(((str(10*i + 2) + " ") * 4).strip())

#d
for _ in range(5):
    print(" ".join(str(x) for x in range(2, 21)))

#e
for _ in range(5):
    print(" ".join(str(x) for x in range(15, 2, -1)))

#ж
for i in range(6, 0, -1):
    print("0 " * i)

#з
for length in range(8, 0, -1):
    print(" ".join(str(x) for x in range(8, 8 - length, -1)))

#и
for start in range(2, 10):
    print(" ".join(str(x) for x in range(start, 11)))

#й
for end in range(2, 11):
   print(" ".join(str(x) for x in range(2, end+1)))
#к
for i in range(3, 7):
    print(((str(i) + " ") * i).strip())

#л
for i in range(21, 26):
    print(((str(i) + " ") * (i - 20)).strip())

#м
for i in range(1, 9):
    print(((str(i) + " ") * (9 - i)).strip())

#н
for i in range(1, 6):
    print(((str(10*i) + " ") * i).strip())

#о
nums = [5,6,7,8,9]
for length in range(5,0,-1):
    print(((str(nums[5-length]) + " ") * length).strip())

#п
nums = [5,10,15,20,25]
for length in range(5,0,-1):
    print(((str(nums[5-length]) + " ") * length).strip())

#р
for i in range(10, 70, 10):
    print(" ".join(str(i + j) for j in range(5)))

#с
for start in [51, 41, 31, 21]:
    print(" ".join(str(x) for x in range(start, start + 8)))

#9.2

# Вариант а)
for j in range(1, 10):  # 1 + j ... 9 + j
    for i in range(1, 10):
        print(f"{i} + {j} = {i + j}", end="   ")
    print()

print()

# Вариант б)
for i in range(1, 10):  # i + 1 ... i + 9
    for j in range(1, 10):
        print(f"{i} + {j} = {i + j}", end="   ")
    print()

#9.3
#Вариант а)
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i*j}", end="  ")
    print()

print()

# Вариант б)
for j in range(1, 10):
    for i in range(1, 10):
        print(f"{i} * {j} = {i*j}", end="  ")
    print()

#9.4
#Вариант а)
n_students = 12
n_subjects = 3
marks = []
print("Введите оценки каждого ученика по 3 предметам (по строкам):")
for i in range(n_students):
    row = list(map(int, input(f"Ученик {i+1}: ").split()))
    while len(row) != n_subjects:
        print(f"Ошибка: введите ровно {n_subjects} оценок.")
        row = list(map(int, input(f"Ученик {i+1}: ").split()))
    marks.append(row)
total_sum = sum(sum(row) for row in marks)
print(f"Сумма всех оценок: {total_sum}")

# Вариант б)

n_students = 12
n_subjects = 3
marks = [[0]*n_subjects for _ in range(n_students)]
print("Введите оценки по предметам (по столбцам), по 12 оценок для каждого предмета:")
for subj in range(n_subjects):
    print(f"Оценки по предмету {subj+1}:")
    for student in range(n_students):
        mark = int(input(f"Ученик {student+1}: "))
        marks[student][subj] = mark
total_sum = sum(sum(row) for row in marks)
print(f"Сумма всех оценок: {total_sum}")

#9.5
n_workers = 12
n_months = 3
salaries = []
for i in range(n_workers):
    row = list(map(int, input(f"Зарплаты работника {i+1} за {n_months} месяцев: ").split()))
    while len(row) != n_months:
        print(f"Введите ровно {n_months} значений")
        row = list(map(int, input(f"Зарплаты работника {i+1}: ").split()))
    salaries.append(row)

# а)
total_sum = sum(sum(row) for row in salaries)
print(f"Общая сумма за квартал: {total_sum}")

# б)
for i, row in enumerate(salaries, 1):
    print(f"Зарплата работника {i} за квартал: {sum(row)}")

# в)
for month in range(n_months):
    month_sum = sum(salaries[worker][month] for worker in range(n_workers))
    print(f"Общая зарплата за месяц {month+1}: {month_sum}")

#9.6
n_athletes = 15
n_programs = 3
results = []
print("Введите результаты спортсменов (баллы по 3 программам):")
for i in range(n_athletes):
    row = list(map(float, input(f"Спортсмен {i+1}: ").split()))
    while len(row) != n_programs:
        print("Введите ровно 3 балла")
        row = list(map(float, input(f"Спортсмен {i+1}: ").split()))
    results.append(row)

# а
for i, row in enumerate(results, 1):
    avg = sum(row)/n_programs
    print(f"Средний балл спортсмена {i}: {avg:.2f}")

# б
for program in range(n_programs):
    avg = sum(results[athlete][program] for athlete in range(n_athletes))/n_athletes
    print(f"Средний балл по программе {program+1}: {avg:.2f}")

#9.7
n_students = 15
n_subjects = 3
grades = []
print("Введите оценки каждого ученика по 3 предметам:")
for i in range(n_students):
    row = list(map(int, input(f"Ученик {i+1}: ").split()))
    while len(row) != n_subjects:
        print(f"Введите роно {n_subjects} оценок")
        row = list(map(int, input(f"Ученик {i+1}: ").split()))
    grades.append(row)

# а) Кол-во пятерок
count_5 = sum(row.count(5) for row in grades)
print(f"Всего пятерок: {count_5}")

# б) Кол-во троек у каждого ученика
for i, row in enumerate(grades, 1):
    print(f"Троек у ученика {i}: {row.count(3)}")

# в) Кол-во двоек по предметам
for subj in range(n_subjects):
    count_2 = sum(1 for student in range(n_students) if grades[student][subj] == 2)
    print(f"Двоек по предмету {subj+1}: {count_2}")

#9.8
n_students = 14
n_subjects = 3
grades = []
print("Введите оценки каждого студента по 3 предметам:")
for i in range(n_students):
    row = list(map(int, input(f"Студент {i+1}: ").split()))
    while len(row) != n_subjects:
        print(f"Введите ровно {n_subjects} оценок")
        row = list(map(int, input(f"Студент {i+1}: ").split()))
    grades.append(row)

# а
count_no_2 = sum(1 for row in grades if 2 not in row)
print(f"Студентов, сдавших без двоек: {count_no_2}")

# б
count_subjects_4_5 = 0
for subj in range(n_subjects):
    subj_grades = [grades[student][subj] for student in range(n_students)]
    if all(g in (4, 5) for g in subj_grades):
        count_subjects_4_5 += 1
print(f"Предметов с оценками только 4 и 5: {count_subjects_4_5}")

#9.9
n_athletes = 8
n_sports = 5
scores = []
print("Введите баллы спортсменов по 5 видам спорта:")
for i in range(n_athletes):
    row = list(map(int, input(f"Спортсмен {i+1}: ").split()))
    while len(row) != n_sports:
        print(f"Введите ровно {n_sports} значений")
        row = list(map(int, input(f"Спортсмен {i+1}: ").split()))
    scores.append(row)

# а
max_score = max(max(row) for row in scores)
print(f"Максимальная оценка: {max_score}")

# б
total_scores = [sum(row) for row in scores]
max_total = max(total_scores)
print(f"Баллы победителя: {max_total}")

#9.10
n_workers = 12
n_months = 3
salaries = []
print("Введите зарплаты работников за 3 месяца:")
for i in range(n_workers):
    row = list(map(int, input(f"Работник {i+1}: ").split()))
    while len(row) != n_months:
        print(f"Введите ровно {n_months} значений")
        row = list(map(int, input(f"Работник {i+1}: ").split()))
    salaries.append(row)

# а
max_salary = max(max(row) for row in salaries)
print(f"Максимальная зарплата: {max_salary}")

# б
total_per_worker = [sum(row) for row in salaries]
max_worker_index = total_per_worker.index(max(total_per_worker)) + 1
print(f"Работник с наибольшей суммой: {max_worker_index}")

# в
total_per_month = [sum(salaries[w][m] for w in range(n_workers)) for m in range(n_months)]
max_month_index = total_per_month.index(max(total_per_month)) + 1
print(f"Месяц с максимальной общей зарплатой: {max_month_index}")

#9.11

# а
for i, row in enumerate(salaries, 1):
    max_month = row.index(max(row)) + 1
    print(f"Работник {i} получил максимальную зарплату в месяце {max_month}")

#
for m in range(n_months):
    month_salaries = [salaries[w][m] for w in range(n_workers)]
    max_worker = month_salaries.index(max(month_salaries)) + 1
    print(f"В месяце {m+1} максимальную зарплату получил работник {max_worker}")

#9.12
n_parallel = 11
n_classes = 4
students = []
print("Введите число учеников в параллелях (классы А Б В Г):")
for i in range(n_parallel):
    row = list(map(int, input(f"Параллель {i+1}: ").split()))
    while len(row) != n_classes:
        print("Введите ровно 4 значения")
        row = list(map(int, input(f"Параллель {i+1}: ").split()))
    students.append(row)

# а
min_class = min(min(row) for row in students)
print(f"Самый малочисленный класс: {min_class}")

# б
parallel_sums = [sum(row) for row in students]
min_parallel_sum = min(parallel_sums)
print(f"Минимальное общее число учеников в параллели: {min_parallel_sum}")

# в
class_sums = [sum(students[i][c] for i in range(n_parallel)) for c in range(n_classes)]
min_class_sum = min(class_sums)
print(f"Минимальное общее число учеников по классам (А, Б, В, Г): {min_class_sum}")

#9.13

# а
for i, row in enumerate(students, 1):
    print(f"Параллель {i}: малочисленный класс = {min(row)}")

# б
for c in range(n_classes):
    col_values = [students[i][c] for i in range(n_parallel)]
    print(f"Малочисленный класс {chr(ord('А') + c)}: {min(col_values)}")

#9.14
donations = []
for shop in range(1, 4):
    shop_data = []
    print(f"Введите доход магазина {shop} за 10 дней:")
    for day in range(1, 11):
        income = float(input(f"День {day}: "))
        shop_data.append(income)
    donations.append(shop_data)

# a
total_per_shop = [sum(shop) for shop in donations]
max_shop_index = total_per_shop.index(max(total_per_shop))
print(f"Магазин {max_shop_index + 1} имеет максимальный общий доход.")

# b
total_per_day = [sum(donations[shop][day] for shop in range(3)) for day in range(10)]
max_day = total_per_day.index(max(total_per_day)) + 1
print(f"День {max_day} имеет максимальный общий доход.")

# c
max_income = 0
shop_of_max = 0
day_of_max = 0
for shop_idx in range(3):
    for day_idx in range(10):
        if donations[shop_idx][day_idx] > max_income:
            max_income = donations[shop_idx][day_idx]
            shop_of_max = shop_idx + 1
            day_of_max = day_idx + 1
print(f"Максимальный доход получен магазином {shop_of_max} в день {day_of_max} с суммой {max_income}.")

#9.15
donations = []
for shop in range(1, 4):
    shop_data = []
    print(f"Введите доход магазина {shop} за 10 дней:")
    for day in range(1, 11):
        income = float(input(f"День {day}: "))
        shop_data.append(income)
    donations.append(shop_data)

# a
for shop_idx, shop_data in enumerate(donations, start=1):
    max_day = shop_data.index(max(shop_data)) + 1
    print(f"Магазин {shop_idx} получил максимум в день {max_day}.")

# б
for day in range(10):
    max_income = -1
    max_shop = 0
    for shop_idx in range(3):
        if donations[shop_idx][day] > max_income:
            max_income = donations[shop_idx][day]
            max_shop = shop_idx + 1
    print(f"День {day + 1}: магазин {max_shop} с максимальным доходом.")

#9.16
students = []
for course in range(1, 7):
    course_data = []
    print(f"Введите количество студентов для курса {course}:")
    total_course_students = 0
    for group in range(1, 7):
        count = int(input(f"Группа {group}: "))
        course_data.append(count)
        total_course_students += count
    students.append(course_data)

# а
total_per_course = [sum(course) for course in students]
min_course_students = min(total_per_course)
min_course_idx = total_per_course.index(min_course_students) + 1
print(f"Курс {min_course_idx} имеет меньше всего студентов: {min_course_students}.")

# б
min_group_size = float('inf')
min_group_info = (0, 0)  # (номер курса, номер группы)
for course_idx, course_data in enumerate(students, start=1):
    for group_idx, count in enumerate(course_data, start=1):
        if count < min_group_size:
            min_group_size = count
            min_group_info = (course_idx, group_idx)
print(f"Самая малочисленная группа: группа {min_group_info[1]} курса {min_group_info[0]}, с численностью {min_group_size}.")

#9.17
prices = []
print("Введите стоимость каждого из 5 видов товара:")
for i in range(5):
    price = float(input(f"Вид {i + 1}: "))
    prices.append(price)
quantities = []
for day in range(6):
    day_data = []
    print(f"Введите количества продаж за день {day+1}:")
    for i in range(5):
        count = int(input(f"Вид {i + 1}: "))
        day_data.append(count)
    quantities.append(day_data)

# а
total_per_type = [0]*5
for day_data in quantities:
    for i in range(5):
        total_per_type[i] += day_data[i]*prices[i]
for i, total in enumerate(total_per_type, start=1):
    print(f"Общий доход от товара {i}: {total}")

# б
for day_idx, day_data in enumerate(quantities, start=1):
    daily_total = sum(day_data[i]*prices[i] for i in range(5))
    print(f"День {day_idx}: общий доход {daily_total}")

# в
total_income = 0
for day_data in quantities:
    total_income += sum(day_data[i]*prices[i] for i in range(5))
print(f"Общий доход магазина за 6 дней: {total_income}")

# г
max_type_index = total_per_type.index(max(total_per_type)) + 1
print(f"Вид товара с максимальным доходом: {max_type_index}")

# д
day_totals = []
for day_idx, day_data in enumerate(quantities, start=1):
    day_total = sum(day_data[i]*prices[i] for i in range(5))
    day_totals.append(day_total)
max_day = day_totals.index(max(day_totals)) + 1
print(f"День {max_day} имел максимальный доход {day_totals[max_day -1]}.")

# е
X = float(input("Введите значение X: "))
count_days = sum(1 for total in day_totals if total > X)
print(f"Количество дней с доходом превышающим {X}: {count_days}")

#9.18
groups = []
for i in range(3):
    print(f"Группа {i+1}")
    total = 0
    for j in range(20):
        score = float(input(f"Введите балл студента {j+1}: "))
        total += score
    avg = total / 20
    groups.append((avg, i+1))
best_group = max(groups, key=lambda x: x[0])
print(f"Лучшая группа: {best_group[1]} с средним баллом {best_group[0]:.2f}")

#9.19
for num in range(120, 141):
    count = 0
    for divisor in range(1, num + 1):
        if num % divisor == 0:
            count += 1
    print(f"{num} делителей: {count}")

#9.20
n = int(input("Введите n: "))
for num in range(1, n + 1):
    divisors = 0
    for divisor in range(1, num + 1):
        if num % divisor == 0:
            divisors += 1
    print(f"{num}" + "+" * divisors)

#9.21
def count_divisors(num):
    count = 0
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            count += 2 if i != num // i else 1
    return count
for num in range(1, 301):
    if count_divisors(num) == 5:
        print(num)

#9.22
for num in range(200, 501):
    if count_divisors(num) == 6:
        print(num)

#9.23
a, b, k = map(int, input("Введите a, b, k: ").split())
for num in range(a, b+1):
    if count_divisors(num) == k:
        print(num)

#9.24
a, b = map(int, input("Введите a и b: ").split())
max_count = 0
max_num = a
min_num = a
for num in range(a, b+1):
    d = count_divisors(num)
    if d > max_count:
        max_count = d
        max_num = num
        min_num = num
    elif d == max_count:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
print(f"Максимальное количество делителей: {max_count}")
print(f"Число с максимальным количеством делителей (большее): {max_num}")
print(f"Число с минимальным количеством делителей (меньшее): {min_num}")

#9.25
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
for num in range(100, 1000):
    if is_prime(num):
        print(num)

#9.26
count = 0
num = 2
primes = []
while count < 100:
    if is_prime(num):
        primes.append(num)
        count += 1
    num += 1
print(primes)

#9.27
def sum_divisors(n):
    total = 0
    for i in range(1, n//2 + 1):
        if n % i == 0:
            total += i
    total += n  # включительно сам число
    return total

for num in range(50, 71):
    print(f"{num}: {sum_divisors(num)}")

#9.28
for num in range(100, 301):
    if sum_divisors(num) == 50:
        print(num)

#9.29
for num in range(300, 601):
    if sum_divisors(num) % 10 == 0:
        print(num)

#9.30
def is_perfect(n):
    total = 0
    for i in range(1, n//2 + 1):
        if n % i == 0:
            total += i
    return total == n
for num in range(100, 1000):
    if is_perfect(num):
        print(num)

#9.31
for num in [6, 28, 496, 8128]:
    print(num)

#9.32
a, b = map(int, input("Введите a и b: ").split())
max_sum = 0
number_with_max_sum = a
for num in range(a, b+1):
    s = sum_divisors(num)
    if s > max_sum:
        max_sum = s
        number_with_max_sum = num
print(f"Число с максимальной суммой делителей: {number_with_max_sum}, сумма: {max_sum}")

#9.33
def sum_divisors_excluding_self(n):
    total = 0
    for i in range(1, n//2 + 1):
        if n % i == 0:
            total += i
    return total
numbers_checked = set()
for num in range(2, 50000):
    if num in numbers_checked:
        continue
    s1 = sum_divisors_excluding_self(num)
    if s1 != num and s1 < 50000:
        s2 = sum_divisors_excluding_self(s1)
        if s2 == num:
            print(f"{num} и {s1}")
            numbers_checked.update([num, s1])

#9.34
n = int(input("Введите n (< 100): "))
ways = []
for count_10 in range(n//10 + 1):
    remaining = n - count_10 * 10
    for count_5 in range(remaining//5 + 1):
        for count_2 in range(remaining//2 + 1):
            sum_used = count_10*10 + count_5*5 + count_2*2
            if sum_used == remaining:
                ways.append((count_2, count_5, count_10))
for idx, (two, five, ten) in enumerate(ways, 1):
    print(f"{idx}: 1 рублей: {n - (two*2 + five*5 + ten*10)} шт., 2 рублей: {two} шт., 5 рублей: {five} шт., 10 рублей: {ten} шт.")

#9.35
banknotes = [1, 2, 4, 8, 16, 32, 64]
def min_banknotes(n):
    result = {}
    for i in range(len(banknotes)):
        count = (n // banknotes[i])
        result[banknotes[i]] = count
        n -= count * banknotes[i]
    return result
n = int(input("Введите n: "))
for amount in range(n, n + 11):
    print(f"Сумма {amount}: {min_banknotes(amount)}")

#9.36
def rectangles_with_area(s, counted=True):
    results = []
    for width in range(1, s + 1):
        if s % width == 0:
            height = s // width
            if counted or width <= height:
                results.append((width, height))
    return results
s = int(input("Введите площадь s: "))
print("Различные прямоугольники (учитываются перестановки):")
for rect in rectangles_with_area(s, counted=True):
    print(rect)
print("Уникальные прямоугольники без учета перестановок:")
for rect in rectangles_with_area(s, counted=False):
    print(rect)

#9.37
def parallelepipeds_with_volume(v, counted=True):
    results = []
    for a in range(1, v + 1):
        for b in range(1, v + 1):
            if a * b != 0 and v % (a * b) == 0:
                c = v // (a * b)
                if counted or (a <= b <= c):
                    results.append((a, b, c))
    return results
v = int(input("Введите объем v: "))
print("Различные параллелепипеды (учитываются перестановки):")
for box in parallelepipeds_with_volume(v, counted=True):
    print(box)
print("Уникальные без учета перестановок:")
for box in parallelepipeds_with_volume(v, counted=False):
    print(box)

#9.38
k = int(input("Введите число k: "))
solutions = []
for x in range(1, 31):
    for y in range(1, 31):
        if x*x + y*y == k*k:
            solutions.append((x, y))
            # x и y считаем одинаковыми решением
print("Решения (x, y):", solutions)

#9.39
m = int(input("Введите m: "))
n = int(input("Введите n: "))
total = 0
for i in range(1, n+1):
    total += i**m
print("Сумма:", total)

#9.40
n = int(input("Введите n: "))
total = sum(i**n for i in range(1, n+1))
print("Сумма:", total)

#9.41
n = int(input("Введите n (до 27): "))
for number in range(100, 1000):
    str_num = str(number)
    sum_digits = sum(int(d) for d in str_num)
    if sum_digits == n:
        print(number)

#9.42
for number in range(100, 1000):
    s = str(number)
    if len(s) == len(set(s)):
        print(number)

#9.43
import math
numbers = [int(input(f"Введите число {i+1}: ")) for i in range(int(input("Введите количество чисел: ")))]
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
g = numbers[0]
for num in numbers[1:]:
    g = gcd(g, num)
print("Наибольший общий делитель:", g)

#9.44
weights = [100, 200, 300, 500, 1000, 1200, 1400, 1500, 2000, 3000]
v = int(input("Введите вес v: "))
count = 0
for mask in range(1 << len(weights)):
    total_weight = 0
    for i in range(len(weights)):
        if mask & (1 << i):
            total_weight += weights[i]
    if total_weight == v:
        count += 1
print("Количество способов:", count)

#9.45
m = int(input("Введите m: "))
n = int(input("Введите n: "))
for x in range(1, n):
    sum_digits = sum(int(d) for d in str(x))
    if sum_digits * sum_digits == m:
        print(x)

#9.46
def digital_root(num):
    while num > 9:
        s = 0
        for d in str(num):
            s += int(d)
        num = s
    return num
number = int(input("Введите число: "))
print("Цифровой корень:", digital_root(number))

#9.47
def solve_bovines():
    total_money = 100
    bull_price = 10
    cow_price = 5
    calf_price = 0.5
    for bulls in range(total_money // bull_price + 1):
        for cows in range((total_money - bulls * bull_price) // cow_price + 1):
            remaining = total_money - bulls * bull_price - cows * cow_price
            if remaining >= 0 and abs(remaining - round(remaining / calf_price) * calf_price) < 1e-9:
                calves = int(round(remaining / calf_price))
                if bulls + cows + calves == 100:
                    print(f"Быков: {bulls}, коров: {cows}, телят: {calves}")
solve_bovines()

#9.48
def prime_factors_unique(n):
    result = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            result.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        result.append(n)
    return list(set(result))
def prime_factors_mult(n):
    result = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            result.append(i)
            n //= i
        i += 1
    if n > 1:
        result.append(n)
    return result
n = int(input("Введите число n: "))
print("Разложение без повторений:")
print(prime_factors_unique(n))
print("Разложение с учетом повторений:")
print(prime_factors_mult(n))

#9.49
def get_prime_factors(n):
    factors = set()
    i = 2
    while i * i <= n:
        if n % i == 0:
            factors.add(i)
            n //= i
        else:
            i += 1
    if n > 1:
        factors.add(n)
    return list(factors)
n = int(input("Введите число n: "))
print("Простые делители:", get_prime_factors(n))

#9.50
import math
n = int(input("Введите число n: "))
coprimes = [x for x in range(1, n) if math.gcd(x, n) == 1]
print("Взаимно простые числа: ", coprimes)

#9.51
import math
n = int(input("Введите число n: "))
p = int(input("Введите число p: "))
coprimes = [x for x in range(1, n) if math.gcd(x, p) == 1]
print("Числа, взаимно простые с p и меньше n:", coprimes)

#9.52
import math
p = int(input("Введите число p: "))
q = int(input("Введите число q: "))
divisors = []
i = 1
while i <= q:
    if q % i == 0 and math.gcd(i, p) == 1:
        divisors.append(i)
    i += 1
print("Делители q, взаимно простые с p:", divisors)

#9.53
def find_smallest_number():
    sums = {}
    min_n = None
    for x in range(1, 101):
        for y in range(x, 101):
            s = x**3 + y**3
            if s in sums:
                sums[s].append((x, y))
            else:
                sums[s] = [(x, y)]
    for n, pairs in sorted(sums.items()):
        if len(pairs) >= 2:
            print(f"{n} = {pairs[0][0]}³ + {pairs[0][1]}³ и {pairs[1][0]}³ + {pairs[1][1]}³")
            return
find_smallest_number()

#9.54
from math import gcd
for denominator in range(2, 8):
    for numerator in range(1, denominator):
        if gcd(numerator, denominator) == 1:
            print(f"{numerator}/{denominator}")

#10.1
import random

# а
print("а) 8 случайных вещественных чисел:")
for _ in range(8):
    print(random.random())

# б
k = int(input("Введите k: "))
print(f"б) {k} случайных вещественных чисел:")
for _ in range(k):
    print(random.random())

# в
print("в) 15 случайных вещественных чисел [25,26):")
for _ in range(15):
    print(25 + random.random())

# г
print("г) 20 случайных вещественных чисел [0,15):")
for _ in range(20):
    print(15 * random.random())

# д
a = int(input("Введите a: "))
b = float(input("Введите b: "))
k = random.randint(1, a)
print(f"д) случайное число k={k}; {k} случайных чисел в диапазоне [0, {b}):")
for _ in range(k):
    print(b * random.random())

# е
print("е) 10 случайных чисел [-40,40):")
for _ in range(10):
    print(-40 + 80 * random.random())

# ж
m = int(input("Введите m: "))
a = float(input("Введите a: "))
b = float(input("Введите b: "))
k = random.randint(1, m)
print(f"ж) k={k}; {k} случайных чисел в диапазоне [{a},{b}):")
for _ in range(k):
    print(a + (b - a) * random.random())

#10.2
# а
print("а) 10 случайных чисел в диапазоне 0..10:")
for _ in range(10):
    print(random.randint(0, 10))

# б
k = int(input("Введите k: "))
a = int(input("Введите a: "))
print(f"б) {k} случайных чисел в диапазоне 0..{a}:")
for _ in range(k):
    print(random.randint(0, a))

# в
print("в) 20 чисел в диапазоне 10..20:")
for _ in range(20):
    print(random.randint(10, 20))

# г
k = int(input("Введите k: "))
a = int(input("Введите a: "))
print(f"г) {k} чисел в диапазоне -10..{a}:")
for _ in range(k):
    print(random.randint(-10, a))

# д
k = random.randint(1, 15)
a = int(input("Введите a: "))
b = int(input("Введите b: "))
print(f"д) k={k}; {k} случайных чисел в диапазоне {a}..{b}:")
for _ in range(k):
    print(random.randint(a, b))

#10.3
m = int(input("Введите m (не превосходящее 20): "))
n = int(input("Введите n (не превосходящее 20): "))
a = int(input("Введите a: "))
b = int(input("Введите b: "))
print(f"М_{m} = {m}")
print(f"Н_{n} = {n}")
print(f"n={n} чисел в диапазоне [{a},{b}]:")
for _ in range(n):
    print(random.randint(a, b))
print(f"Массив из {m} неотрицательных чисел, не превосходящих {n}:")
for _ in range(m):
    print(random.uniform(0, n))

#10.4
print("50 целых чисел в диапазоне 0..3 (только 0 и 1):")
for _ in range(50):
    num = random.randint(0, 3)
    if num in [0, 1]:
        print(num)

#10.5
print("30 целых чисел в диапазоне 0..5 (только нечетные):")
for _ in range(30):
    num = random.randint(0, 5)
    if num % 2 == 1:
        print(num)

#10.6
zeros = 0
ones = 0
for _ in range(50):
    bit = random.randint(0, 1)
    if bit == 0:
        zeros += 1
    else:
        ones += 1
print(f"Количество нулей: {zeros}")
print(f"Количество единиц: {ones}")

#10.7
# а
a = random.randint(0, 1)
b = random.randint(0, 2)
while b == a:
    b = random.randint(0, 2)
print(f"а) a={a}, b={b}")

# б
a = random.randint(1, 2)
b = random.randint(0, 2)
while b == a:
    b = random.randint(0, 2)
c = random.randint(1, 3)
while c == a or c == b:
    c = random.randint(1, 3)
print(f"б) a={a}, b={b}, c={c}")

# в
numbers = [2]*7 + [3]*8
random.shuffle(numbers)
print("в) 15 чисел (7 двоек и 8 троек):")
print(numbers)

#10.8
result = random.randint(0, 1)
if result == 0:
    print("Орел")
else:
    print("Решка")

#10.9
import random
def частоты(подбрасывания):
    count_0 = 0
    count_1 = 0
    for _ in range(подбрасывания):
        результат = random.randint(0, 1)
        if результат == 0:
            count_0 += 1
        else:
            count_1 += 1
    freq_0 = count_0 / подбрасывания
    freq_1 = count_1 / подбрасывания
    return freq_0, freq_1
for n in [100, 1000]:
    freq_0, freq_1 = частоты(n)
    print(f"При {n} подбрасываниях:")
    print(f"Относительная частота 0: {freq_0:.2f}")
    print(f"Относительная частота 1: {freq_1:.2f}\n")

#10.10
#a)
import random
def игра_один_раз():
    ответ = int(input("Чет (введите 2) или нечет (введите 1)? "))
    компьютерное_число = random.randint(1, 2)
    print(f"Компьютер выбрал: {компьютерное_число}")
    if ответ == компьютерное_число:
        print("Вы выиграли!")
    else:
        print("Вы проиграли!")

#b)
import random
def игра_несколько_раз(n):
    счет_ваш = 0
    счет_комп = 0
    for _ in range(n):
        ответ = int(input("Чет (введите 2) или нечет (введите 1)? "))
        компьютерное_число = random.randint(1, 2)
        print(f"Компьютер выбрал: {компьютерное_число}")
        if ответ == компьютерное_число:
            счет_ваш += 1
        else:
            счет_комп += 1
    if счет_ваш > счет_комп:
        победитель = "Вы"
        счет_выигрыш = счет_ваш
    elif счет_ваш < счет_комп:
        победитель = "Компьютер"
        счет_выигрыш = счет_комп
    else:
        победитель = "Ничья"
        счет_выигрыш = счет_ваш
    print(f"Результат: счет {счет_ваш}:{счет_комп}")
    if победитель != "Ничья":
        print(f"{победитель} выиграл!")
    else:
        print("Ничья!")

#v
import random
def игра_до_отказа():
    счет_ваш = 0
    счет_комп = 0
    while True:
        ответ = int(input("Чет (введите 2) или нечет (введите 1)? "))
        компьютерное_число = random.randint(1, 2)
        print(f"Компьютер выбрал: {компьютерное_число}")
        if ответ == компьютерное_число:
            счет_ваш += 1
        else:
            счет_комп += 1
        продолжить = input("Продолжить еще раз? (да/нет): ").lower()
        if продолжить != 'да':
            break
    print(f"Итог: {счет_ваш} - ваши победы, {счет_комп} - победы компьютера.")
    if счет_ваш > счет_комп:
        print("Вы выиграли!")
    elif счет_ваш < счет_комп:
        print("Вы проиграли!")
    else:
        print("Ничья!")
игра_до_отказа()

#10.11
import random
кубик_число = random.randint(1, 6)
print(f"Выпавшее число: {кубик_число}")

#10.12
import random
игрок_1 = random.randint(1, 6)
игрок_2 = random.randint(1, 6)
print(f"Игрок 1 выбросил: {игрок_1}")
print(f"Игрок 2 выбросил: {игрок_2}")
if игрок_1 > игрок_2:
    print("Победил игрок 1")
elif игрок_2 > игрок_1:
    print("Победил игрок 2")
else:
    print("Ничья")

#10.13
import random
def игра_один_раз():
    очки_1 = random.randint(1, 6) + random.randint(1, 6)
    очки_2 = random.randint(1, 6) + random.randint(1, 6)
    print(f"Игрок 1 набрал: {очки_1}")
    print(f"Игрок 2 набрал: {очки_2}")
    if очки_1 > очки_2:
        print("Выиграл игрок 1")
    elif очки_2 > очки_1:
        print("Выиграл игрок 2")
    else:
        print("Ничья")
игра_один_раз()

#10.14
import random
def бросить_кубики(количество_кубиков):
    return [random.randint(1, 6) for _ in range(количество_кубиков)]
def основная():
    K = int(input("Введите число кубиков для каждого игрока: "))
    очки_игроков = []
    for i in range(1, 4):
        броски = бросить_кубики(K)
        сумма = sum(броски)
        очки_игроков.append((i, сумма))
        print(f"Игрок {i} бросил: {броски}, сумма очков: {сумма}")
    победитель = max(очки_игроков, key=lambda x: x[1])
    print(f"Победил игрок {победитель[0]} с суммой {победитель[1]}.")
if __name__ == "__main__":
    основная()

#10.15
import random
def подсчет_частот(число_бросков):
    частоты = {число: 0 for число in range(1, 7)}
    for _ in range(число_бросков):
        результат = random.randint(1, 6)
        частоты[результат] += 1
    # Вывод относительной частоты
    print(f"Результаты при {число_бросков} бросках:")
    for число in range(1, 7):
        относительная = частоты[число] / число_бросков
        print(f"Число {число}: {частоты[число]} раз, относительная частота: {относительная:.2f}")
подсчет_частот(100)
print()
подсчет_частот(1000)

#10.16
import random
def выбрать_кость():
    стороны = list(range(0, 7))
    сторон1 = random.choice(стороны)
    сторон2 = random.choice(стороны)
    print(f"Выбрана кость {сторон1}–{сторон2}")
if __name__ == "__main__":
    выбрать_кость()

#10.17
import random

#а
def variant_a():
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    print(f"Чему равно произведение {a}×{b}?")
    answer = int(input())
    if answer == a * b:
        print("Ответ правильный.")
    else:
        print(f"Ответ неправильный. Правильный ответ: {a * b}")

#б
def variant_b():
    correct = 0
    incorrect = 0
    for _ in range(20):
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        print(f"Чему равно произведение {a}×{b}?")
        answer = int(input())
        if answer == a * b:
            print("Ответ правильный.")
            correct += 1
        else:
            print(f"Ответ неправильный. Правильный ответ: {a * b}")
            incorrect += 1
    print(f"Количество правильных ответов: {correct}")
    print(f"Количество неправильных ответов: {incorrect}")

#в
def variant_c():
    while True:
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        print(f"Чему равно произведение {a}×{b}? (Введите 0 для выхода)")
        answer = int(input())
        if answer == 0:
            print("Выход из программы.")
            break
        elif answer == a * b:
            print("Ответ правильный.")
        else:
            print(f"Ответ неправильный. Правильный ответ: {a * b}")
