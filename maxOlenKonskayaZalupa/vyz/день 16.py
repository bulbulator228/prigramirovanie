#7.81
numbers = [input("Введите число: ") for _ in range(20)]
hits_missed_counts = []
for num in numbers:
    if len(num) == 1:
        hits_missed_counts.append((int(num), 0))
    elif len(num) == 2:
        hits_missed_counts.append((int(num[0]), int(num[1])))
    else:
        print("Некорректный формат числа:", num)
equal_scores = sum(1 for gm, pm in hits_missed_counts if gm == pm)
print("Количество игр с равными счетом:", equal_scores)

#7.82
n = int(input("Введите n: "))
a = [int(input(f"Введите число {i+1}: ")) for i in range(n)]

# а
count_equal_pairs = sum(1 for i in range(n - 1) if a[i] == a[i + 1])

# б
count_zero_pairs = sum(1 for i in range(n - 1) if a[i] == 0 and a[i + 1] == 0)

# в
count_even_pairs = sum(1 for i in range(n - 1) if a[i] % 2 == 0 and a[i + 1] % 2 == 0)

# г
count_fives = sum(1 for i in range(n - 1) if abs(a[i]) % 10 == 5 and abs(a[i + 1]) % 10 == 5)
print("Равных пар:", count_equal_pairs)
print("Пары с нулями:", count_zero_pairs)
print("Пары с четными числами:", count_even_pairs)
print("Пары, оканчивающиеся на 5:", count_fives)

#7.83
numbers = list(map(int, input("Введите числа через пробел: ").split()))
has_even = any(num % 2 == 0 for num in numbers)
print("Есть хотя бы одно четное число:", "Да" if has_even else "Нет")

#7.84
a = [int(input(f"Введите число {i+1}: ")) for i in range(10)]
positive_count = sum(1 for num in a if num > 0)
print("Количество положительных чисел не превышает 5:", positive_count <= 5)

#7.85
x = [float(input(f"Введите число {i+1}: ")) for i in range(15)]
count = sum(1 for num in x if num <= 33.2)
print("Количество чисел, не больше 33,2, кратно 4:", count % 4 == 0)

#7.86
c = [int(input(f"Введите число {i+1}: ")) for i in range(int(input("Введите n: ")))]
count_less_20 = sum(1 for num in c if num < 20)
print("Количество чисел меньше 20 равно 5:", count_less_20 == 5)

#7.87
d = [int(input(f"Введите число {i+1}: ")) for i in range(int(input("Введите m: ")))]
pos_count = sum(1 for num in d if num > 0)
print("Количество положительных чисел кратно 3:", pos_count % 3 == 0)

#7.88
n = int(input("Введите n: "))
x = int(input("Введите x: "))
a = [int(input(f"Введите число {i+1}: ")) for i in range(n)]
neg_count = sum(1 for num in a if num < 0)
print("Количество отрицательных чисел больше x:", neg_count > x)

#7.89
m = int(input("Введите m: "))
p = int(input("Введите p: "))
a = [int(input(f"Введите число {i+1}: ")) for i in range(int(input("Введите m (длина): ")))]
count_greater_m = sum(1 for num in a if num > m)
print("Количество чисел, больше m, кратно p:", count_greater_m % p == 0)

#7.90
grades = list(map(int, input("Введите 12 оценок через пробел: ").split()))
no_threes = all(grade != 3 for grade in grades)
print("Нет троек:", "Да" if no_threes else "Нет")

#7.91
precipitations = list(map(int, input("Введите количество осадков за каждый день марта: ").split()))
days_no_precip = sum(1 for p in precipitations if p == 0)
print("Осадков не было 10 дней:", days_no_precip >= 10)

#7.92
grades = [int(input(f"Оценка ученика {i+1}: ")) for i in range(28)]
has_two = 2 in grades
print("Есть двойка:", "Да" if has_two else "Нет")

#7.93
powers = [int(input(f"Мощность модели {i+1}: ")) for i in range(30)]
exists_power_above_200 = any(power > 200 for power in powers)
print("Модель с мощностью выше 200 л. с. есть:", "Да" if exists_power_above_200 else "Нет")

# 7.94
sequence = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
count = 0
for i in range(1, len(sequence) - 1):
    if sequence[i] > sequence[i - 1] and sequence[i] > sequence[i + 1]:
        count += 1
print("Количество строгих локальных максимумов:", count)

# 7.95
sequence = list(map(int, input("Введите последовательность ненулевых целых чисел через пробел: ").split()))
changes = 0
for i in range(1, len(sequence)):
    if sequence[i] * sequence[i - 1] < 0:
        changes += 1
print("Количество изменений знака:", changes)

# 7.96
sequence = []
for i in range(15):
    num = int(input(f"Введите натуральное число {i+1}: "))
    sequence.append(num)
pair_found = False
for i in range(len(sequence) - 1):
    if sequence[i] == sequence[i + 1]:
        print(f"Пара одинаковых соседних чисел на позициях {i+1} и {i+2}")
        pair_found = True
        break
if not pair_found:
    print("Одинаковых соседних чисел не найдено.")

# 7.97
sequence = []
print("Введите числа, для завершения введите -1:")
while True:
    num = int(input())
    if num == -1:
        break
    sequence.append(num)

if len(sequence) < 2:
    print("Последовательность должна содержать как минимум два числа.")
else:
    pair_found = False
    for i in range(len(sequence) - 1):
        if sequence[i] == sequence[i + 1]:
            print(f"Пара одинаковых соседних чисел на позициях {i+1} и {i+2}")
            pair_found = True
            break
    if not pair_found:
        print("Одинаковых соседних чисел не найдено.")

# 7.98
sequence = []
for i in range(20):
    num = int(input(f"Введите натуральное число {i+1}: "))
    sequence.append(num)

pair_found = False
for i in range(len(sequence) - 1):
    if sequence[i] % 2 != 0 and sequence[i + 1] % 2 != 0:
        print(f"Пара соседних нечетных чисел на позициях {i+1} и {i+2}")
        pair_found = True
        break
if not pair_found:
    print("Соседних нечетных чисел не найдено.")

# 7.99
sequence = []
print("Введите числа, для завершения введите 9999:")
while True:
    num = int(input())
    if num == 9999:
        break
    sequence.append(num)

if len(sequence) < 2:
    print("Последовательность должна содержать как минимум два числа.")
else:
    pair_found = False
    for i in range(len(sequence) - 1):
        if sequence[i] % 2 == 0 and sequence[i + 1] % 2 == 0:
            print(f"Пара соседних чётных чисел на позициях {i+1} и {i+2}")
            pair_found = True
            break
    if not pair_found:
        print("Соседних четных чисел не найдено.")

# 7.100
sequence = list(map(float, input("Введите 15 вещественных чисел через пробел: ").split()))
for i in range(len(sequence) - 1):
    if sequence[i] > sequence[i + 1]:
        print(f"Последовательность нарушает возрастание на позиции {i+1}.")
        break
else:
    print("Последовательность является упорядоченной по возрастанию.")

#7.101
sequence = []
while True:
    x = float(input("Введите число: "))
    if x == 10000:
        break
    sequence.append(x)
is_sorted = True
first_violation_index = -1
for i in range(len(sequence) - 1):
    if sequence[i] > sequence[i + 1]:
        is_sorted = False
        first_violation_index = i + 1  # порядковый номер (начиная с 1)
        break
if is_sorted:
    print("Последовательность упорядочена по возрастанию.")
else:
    print(f"Последовательность не упорядочена. Первый нарушающий элемент - номер {first_violation_index}.")

#7.102
growths = []
while True:
    g = float(input("Введите рост ученика: "))
    growths.append(g)
    if len(growths) >= 2 and g == 0:
        break
if growths[-1] == 0:
    growths.pop()
is_descending = True
for i in range(len(growths) - 1):
    if growths[i] < growths[i + 1]:
        is_descending = False
        break
if is_descending:
    print("Ученики перечислены в порядке убывания роста.")
else:
    print("Ученики не перечислены в порядке убывания роста.")

#7.103
scores = []
while True:
    s = float(input("Введите сумму очков команды: "))
    scores.append(s)
    if len(scores) >= 2 and s == 0:
        break
if scores[-1] == 0:
    scores.pop()
is_sorted = all(scores[i] > scores[i + 1] for i in range(len(scores) - 1))
if is_sorted:
    print("Команды перечислены по порядку в соответствии с занятыми местами.")
else:
    print("Команды не перечислены по порядку в соответствии с занятыми местами.")

#7.104
x = []
for _ in range(12):
    x.append(int(input("Введите число: ")))
all_equal = all(elem == x[0] for elem in x)
print("Все элементы равны между собой." if all_equal else "Элементы не равны между собой.")

#7.105
sequence = []
while True:
    num = int(input("Введите число: "))
    sequence.append(num)
    if num < 0:
        break
if len(sequence) > 0:
    all_equal = all(elem == sequence[0] for elem in sequence)
    print("Все элементы равны между собой." if all_equal else "Элементы не равны между собой.")
else:
    print("Последовательность пустая.")

#7.106
numbers = [float(input("Введите число: ")) for _ in range(16)]
sum_greater_than_20 = 0
count = 0
for c in numbers:
    if c > 20:
        sum_greater_than_20 += c
        count += 1
average = sum_greater_than_20 / count
print(f"Среднее арифметическое чисел, больших 20: {average}")

#7.107
n = int(input("Введите число n: "))
a = [int(input(f"Введите число a{i+1}: ")) for i in range(12)]
greater_than_n = [num for num in a if num > n]
average = sum(greater_than_n) / len(greater_than_n)
print(f"Среднее арифметическое чисел, больших {n}: {average}")

#7.108
m = int(input("Введите натуральное число m: "))
n = int(input("Введите число n: "))
b = [int(input(f"Введите число b{i+1}: ")) for i in range(m)]
multiples = [num for num in b if num % n == 0]
average = sum(multiples) / len(multiples)
print(f"Среднее арифметическое чисел, кратных {n}: {average}")

#7.109
numbers = [int(input(f"Введите число {i+1}: ")) for i in range(12)]
even_sum = 0
even_count = 0
odd_sum = 0
odd_count = 0
for num in numbers:
    if num % 2 == 0:
        even_sum += num
        even_count += 1
    else:
        odd_sum += num
        odd_count += 1
avg_even = even_sum / even_count if even_count > 0 else 0
avg_odd = odd_sum / odd_count if odd_count > 0 else 0
print(f"Среднее арифметическое четных чисел: {avg_even}")
print(f"Среднее арифметическое нечетных чисел: {avg_odd}")

#7.110
masses = []
while True:
    m = float(input("Введите массу человека: "))
    masses.append(m)
    if m > 100:
        continue
    elif len(masses) >= 2 and input("Закончить ввод? (да/нет): ").lower() == 'да':
        break
full_masses = [mass for mass in masses if mass > 100]
others_masses = [mass for mass in masses if mass <= 100]
average_full = sum(full_masses) / len(full_masses) if len(full_masses) > 0 else 0
average_others = sum(others_masses) / len(others_masses) if len(others_masses) > 0 else 0
print(f"Средняя масса полных людей: {average_full}")
print(f"Средняя масса остальных людей: {average_others}")

#7.111
growths = []
males = []
females = []
n = int(input("Введите число учеников: "))
for i in range(n):
    g = float(input(f"Введите рост ученика {i+1} (отрицательное - мальчик): "))
    growths.append(g)
    if g < 0:
        males.append(g)
    else:
        females.append(g)
avg_male = sum(males) / len(males) if len(males) > 0 else 0
avg_female = sum(females) / len(females) if len(females) > 0 else 0
print(f"Средний рост мальчиков: {avg_male}")
print(f"Средний рост девочек: {avg_female}")
