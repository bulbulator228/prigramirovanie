#7.112
b = list(map(float, input("Введите 15 чисел через пробел: ").split()))
count = 0
suma = 0.0
for num in b:
    if num > 10:
        suma += num
        count += 1
if count > 0:
    print("Среднее арифметическое чисел, больших 10:", suma / count)
else:
    print("Чисел, больших 10, нет.")

#7.113
x = int(input("Введите натуральное число x: "))
a = list(map(int, input("Введите 12 чисел через пробел: ").split()))
n = int(input("Введите число n: "))
filtered = [num for num in a if num > n]
if len(filtered) > 0:
    print("Среднее арифметическое чисел, больших n:", sum(filtered) / len(filtered))
else:
    print("Нет чисел, больших n.")

#7.114
d = list(map(int, input("Введите 14 чисел через пробел: ").split()))
even_numbers = [num for num in d if num % 2 == 0]
if len(even_numbers) > 0:
    print("Среднее арифметическое чётных чисел:", sum(even_numbers) / len(even_numbers))
else:
    print("Чётных чисел среди заданных нет.")

#7.115
m = int(input("Введите натуральное число m: "))
a = list(map(int, input(f"Введите {m} чисел через пробел: ").split()))
n = int(input("Введите число n: "))
filtered = [num for num in a if num % n == 0]
if len(filtered) > 0:
    print("Среднее арифметическое чисел, кратных n:", sum(filtered) / len(filtered))
else:
    print("Нет чисел, кратных n.")

#7.116
num_cars = int(input("Количество марок автомобилей: "))
car_costs = []
for _ in range(num_cars):
    cost = float(input("Введите стоимость автомобиля: "))
    car_costs.append(cost)
num_motos = int(input("Количество марок мотоциклов: "))
moto_costs = []
for _ in range(num_motos):
    cost = float(input("Введите стоимость мотоцикла: "))
    moto_costs.append(cost)
average_cars = sum(car_costs) / len(car_costs)
average_motos = sum(moto_costs) / len(moto_costs)
if average_cars > 3 * average_motos:
    print("Средняя стоимость автомобилей превышает среднюю стоимость мотоциклов более чем в 3 раза.")
else:
    print("Условие не выполняется.")

#7.117
n = int(input("Введите число учеников: "))
growths = list(map(float, input(f"Введите рост каждого ученика через пробел: ").split()))
boys = [growths[i] for i in range(n) if i % 2 == 0]  # условно мальчики - чётные индексы
girls = [growths[i] for i in range(n) if i % 2 != 0]
if len(boys) > 0 and len(girls) > 0:
    mean_boys = sum(boys) / len(boys)
    mean_girls = sum(girls) / len(girls)
    if mean_boys - mean_girls > 10:
        print("Средний рост мальчиков превышает средний рост девочек более чем на 10 см.")
    else:
        print("Условие не выполняется.")
else:
    print("Недостаточно данных для сравнения.")

#7.118
n = int(input("Введите натуральное число n: "))
a = list(map(int, input(f"Введите {n} чисел через пробел: ").split()))

# a
last_index = -1
for i in range(n - 1, -1, -1):
    if a[i] == 10:
        last_index = i + 1  # номера с 1
        break
if last_index != -1:
    print("Номер последнего числа 10:", last_index)
else:
    print("Чисел 10 нет.")

# б
first_index = -1
for i in range(n):
    if a[i] == 10:
        first_index = i + 1
        break
if first_index != -1:
    print("Номер первого числа 10:", first_index)
else:
    print("Чисел 10 нет.")

#7.119
n = int(input("Введите натуральное число n: "))
b = list(map(int, input(f"Введите {n} чисел через пробел: ").split()))
last_index = -1
for i in range(n):
    if b[i] > 100:
        last_index = i + 1
print("Номер последнего числа, большего 100:", last_index)

#7.120
n = int(input("Введите натуральное число n: "))
c = list(map(int, input(f"Введите {n} чисел через пробел: ").split()))
last_index = -1
for i in range(n):
    if c[i] == 25:
        last_index = i + 1
print("Номер последнего числа, равного 25:", last_index)

#7.121
k = int(input("Введите натуральное число k: "))
b = list(map(int, input(f"Введите {k} чисел через пробел: ").split()))
last_neg_index = -1
for i in range(k):
    if b[i] < 0:
        last_neg_index = i + 1
print("Номер последнего отрицательного числа:", last_neg_index)

#7.122
m = int(input("Введите натуральное число m: "))
x = list(map(int, input(f"Введите {m} чисел через пробел: ").split()))
last_index = -1
for i in range(m):
    if str(x[i]).endswith("12"):
        last_index = i + 1
print("Номер последнего числа, оканчивающегося на 12:", last_index)

#7.123
heights = []
for i in range(15):
    h = float(input(f"Введите рост ученика {i+1}: "))
    heights.append(h)
heights.sort(reverse=True)
new_height = float(input("Введите рост нового ученика: "))
from bisect import bisect_left
position = bisect_left(heights[::-1], new_height)
index_in_list = 15 - position
print(f"Рост нового ученика займет место {index_in_list + 1} в перечне.")

#7.124
scores = []
for i in range(20):
    score = int(input(f"Введите очки команды {i+1}: "))
    scores.append(score)
scores.sort(reverse=True)
N = int(input("Введите число очков N: "))
import bisect
position = bisect.bisect_left(scores[::-1], N)
rank = 20 - position
print(f"Команда, набравшая {N} очков, занимает  {rank} место.")

#7.125
y = []
for i in range(15):
    y.append(float(input(f"Введите число {i+1} y{i+1}: ")))
y.sort()
n = float(input("Введите число n: "))

# а
import bisect
pos = bisect.bisect_left(y, n)
sum_less_than_n = sum(y[:pos])
print(f"Сумма чисел, меньших {n}: {sum_less_than_n}")

# б
lower_idx = pos - 1
upper_idx = pos
print(f"n находится между y{lower_idx + 1} = {y[lower_idx]} и y{upper_idx + 1} = {y[upper_idx]}")
print(f"Индексы: {lower_idx + 1} и {upper_idx + 1}")

#7.126
a = []
found_negative = False
first_negative_index = None
for i in range(15):
    num = float(input(f"Введите число {i+1} a{i+1}: "))
    a.append(num)
import itertools
negatives = list(filter(lambda x: x < 0, enumerate(a, start=1)))
if negatives:
    first_negative_index = negatives[0][0]
    print(f"Есть отрицательное число. Первый отрицательный на позиции {first_negative_index}.")
else:
    print("Отрицательных чисел в последовательности нет.")

#7.127
sequence = []
index_of_666 = None
while True:
    num = int(input("Введите число: "))
    sequence.append(num)
    if num == 100:
        break
index_of_666 = list(filter(lambda x: sequence[x] == 666, range(len(sequence))))
if index_of_666:
    print(f"Первое вхождение числа 666 на позиции {index_of_666[0] + 1}.")
else:
    print("Число 666 в последовательности отсутствует.")

#7.128
b = []
index_with_7 = None
for i in range(12):
    num = int(input(f"Введите число {i+1} b{i+1}: "))
    b.append(num)
matching = list(filter(lambda x: x % 10 == 7, range(len(b))))
if matching:
    index_with_7 = matching[0]
    print(f"Число, оканчивающееся на 7, находится на позиции {index_with_7 + 1}.")
else:
    print("Таких чисел нет.")

#7.129
sequence = []
for i in range(20):
    num = float(input(f"Введите число {i+1}: "))
    sequence.append(num)
from itertools import groupby
count_repeats = 0
for key, group in groupby(sequence):
    group_list = list(group)
    if len(group_list) > 1:
        count_repeats += len(group_list)
print(f"Количество повторяющихся чисел: {count_repeats}")

#7.130
sequence = []
for i in range(20):
    num = float(input(f"Введите число {i+1}: "))
    sequence.append(num)
count = 0
for i in range(19):
    if sequence[i] == sequence[i + 1]:
        count += 1
print(f"Количество чисел, идущих подряд и равных: {count}")

#7.131
sequence = list(map(int, input("Введите 20 чисел: ").split()))
count = 1
total = 0
for i in range(1, len(sequence)):
    if sequence[i] == sequence[i - 1]:
        count += 1
    else:
        total += count
        count = 1
total += count
print("Количество чисел, идущих подряд, равных между собой:", total)

#7.132
sequence = list(map(int, input("Введите 30 чисел: ").split()))
unique_numbers = set(sequence)
print("Количество различных чисел:", len(unique_numbers))

#7.133
sequence = []
while True:
    num = float(input("Введите число (если последний, то 1000): "))
    sequence.append(num)
    if num == 1000:
        break
count = 1
total = 1
for i in range(1, len(sequence)):
    if sequence[i] == sequence[i - 1]:
        count += 1
    else:
        total += count
        count = 1
print("Количество таких чисел:", total)

#7.134
sequence = []
while True:
    num = float(input("Введите число (если последний, то 0): "))
    sequence.append(num)
    if num == 0:
        break
distinct_numbers = []
for num in sequence:
    if num not in distinct_numbers:
        distinct_numbers.append(num)
print("Количество различных чисел:", len(distinct_numbers))

#7.135
n = int(input("Введите натуральное число n: "))
numbers = []
max_num = float('-inf')
min_num = float('inf')
for _ in range(15):
    x = float(input("Введите вещественное число: "))
    numbers.append(x)
    if x > max_num:
        max_num = x
    if x < min_num:
        min_num = x
print("а) Максимальное число:", max_num)
print("б) Минимальное число:", min_num)
print("в) Максимальное и минимальное:", max_num, min_num)

#7.136
best_time = None
while True:
    time_str = input("Введите результат спортсмена (или 'стоп' для завершения): ")
    if time_str.lower() == 'стоп':
        break
    time = float(time_str)
    if best_time is None or time < best_time:
        best_time = time
    print("Лучший результат:", best_time)

#7.137
distances = list(map(float, input("Введите расстояния до городов через пробел: ").split()))
max_distance = max(distances)
print("Самое удаленное расстояние:", max_distance)

#7.138
temperatures = list(map(float, input("Введите температуры за каждый день месяца: ").split()))
max_temp = max(temperatures)
print("Максимальная температура месяца:", max_temp)

#7.139
speeds = list(map(float, input("Введите максимальные скорости 20 автомобилей: ").split()))
max_speed = max(speeds)
print("Максимальная скорость самого быстрого автомобиля:", max_speed)

#7.140
areas = list(map(float, input("Введите площади кругов: ").split()))
min_area = min(areas)
import math
radius = math.sqrt(min_area / math.pi)
print("Радиус самого маленького круга:", radius)

#7.141
areas = list(map(float, input("Введите площади квадратов: ").split()))
max_area = max(areas)
import math
diagonal = math.sqrt(2 * max_area)
print("Диагональ самого большого квадрата:", diagonal)

#7.142
masses = list(map(float, input("Введите массы 20 тел: ").split()))
volumes = list(map(float, input("Введите объемы 20 тел: ").split()))
densities = [m / v for m, v in zip(masses, volumes)]
max_density = max(densities)
print("Максимальная плотность материала:", max_density)