#7.143
n = 16
populations = []
areas = []
for i in range(n):
    p, a = map(float, input(f"Введите численность и площадь страны {i+1} через пробел: ").split())
    populations.append(p)
    areas.append(a)
densities = [pop/area for pop, area in zip(populations, areas)]

min_density = min(densities)
print(f"Минимальная плотность населения: {min_density}")

#7.144
n = int(input("Введите количество пар n: "))
pairs = []
for i in range(n):
    a, b = map(int, input(f"Введите пару {i+1} через пробел: ").split())
    pairs.append((a, b))
max_sum = max(a + b for a, b in pairs)
min_product = min(a * b for a, b in pairs)
print(f"Максимальная сумма: {max_sum}")
print(f"Минимальное произведение: {min_product}")

#7.145
n = int(input("Введите число оценок: "))
scores = list(map(float, input("Введите оценки через пробел: ").split()))
from collections import Counter
counter = Counter(scores)
max_score = max(scores)
min_score = min(scores)
scores.remove(max_score)
scores.remove(min_score)
average_score = sum(scores) / len(scores) if scores else 0
print(f"Оценка для зачета: {average_score}")


#7.146
heights = list(map(float, input("Введите рост каждого человека через пробел: ").split()))
max_height = max(heights)
min_height = min(heights)
difference = max_height - min_height
print(f"Разница в росте: {difference}")

#7.147
import random
classes = [int(input(f"Введите число учеников в {i+1}-ом классе: ")) for i in range(20)]
max_class = max(classes)
min_class = min(classes)
difference = max_class - min_class
print(f"Разница между численностью самого большого и малого класса: {difference}")

#7.148
a = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
max_a = max(a)
min_a = min(a)
if max_a - min_a <= 25:
    print("Верно, максимум не превышает минимум более чем на 25.")
else:
    print("Некорректно, максимум превышает минимум более чем на 25.")

#7.149
masses = list(map(float, input("Введите массы каждого человека через пробел: ").split()))
max_mass = max(masses)
min_mass = min(masses)
if max_mass > 2 * min_mass:
    print("Масса самого тяжелого превышает массу самого легкого более чем в 2 раза.")
else:
    print("Масса самого тяжелого НЕ превышает массу самого легкого более чем в 2 раза.")

#7.150
n = int(input("Введите число элементов последовательности: "))
sequence = list(map(int, input("Введите последовательность через пробел: ").split()))
max_length = 0
current_length = 0
for num in sequence:
    if num % 2 == 0:
        current_length += 1
        max_length = max(max_length, current_length)
    else:
        current_length = 0
print(f"Наибольшая длина отрезка из четных чисел: {max_length}")

#7.151
n = int(input("Введите число элементов последовательности: "))
sequence = list(map(int, input("Введите последовательность из 0 и 1 через пробел: ").split()))
min_length = None
current_length = 0
for num in sequence:
    if num == 0:
        current_length += 1
        if min_length is None or current_length < min_length:
            min_length = current_length
    else:
        current_length = 0
if min_length is not None:
    print(f"Наименьшая длина отрезка из нулей: {min_length}")
else:
    print("В последовательности нет нулевых отрезков.")

#7.152
a = [1.5, 2.3, 3.7, 4.0, 5.5, 6.1, 7.8, 8.9, 9.4, 10.0, 11.2, 12.5, 13.3, 14.7, 15.2]  # пример, можно вводить
n = float(input("Введите число n: "))
import bisect
pos = bisect.bisect_left(a, n)
neighbors = []
if pos > 0:
    neighbors.append((abs(a[pos - 1] - n), pos - 1))
if pos < len(a):
    neighbors.append((abs(a[pos] - n), pos))
closest = min(neighbors, key=lambda x: x[0])
index = closest[1]
value = a[index]
print(f"Ближайший элемент: номер {index + 1}, значение {value}")

#7.153
numbers = []
for _ in range(14):
    num = int(input("Введите число: "))
    numbers.append(num)
max_even = None
for num in numbers:
    if num % 2 == 0:
        if max_even is None or num > max_even:
            max_even = num
if max_even is not None:
    print("Максимальное четное число:", max_even)
else:
    print("Четных чисел среди заданных нет.")

#7.154
sequence = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
max_count = 1
current_count = 1
for i in range(1, len(sequence)):
    if sequence[i] == sequence[i - 1]:
        current_count += 1
        if current_count > max_count:
            max_count = current_count
    else:
        current_count = 1
print("Наибольшее количество подряд идущих одинаковых элементов:", max_count)

#7.155
sequence = list(map(int, input("Введите последовательность чисел: ").split()))
max_length = 1
current_length = 1
for i in range(1, len(sequence)):
    if sequence[i] > sequence[i - 1]:
        current_length += 1
        if current_length > max_length:
            max_length = current_length
    else:
        current_length = 1
print("Наибольшая длина монотонно возрастающего фрагмента:", max_length)

#7.156
#a
n = int(input("Введите количество чисел: "))
sequence = []
for _ in range(n):
    sequence.append(int(input("Введите число: ")))
max_length_increasing = 1
max_length_decreasing = 1
current_length_inc = 1
current_length_dec = 1
for i in range(1, n):
    if sequence[i] > sequence[i - 1]:
        current_length_inc += 1
        if current_length_inc > max_length_increasing:
            max_length_increasing = current_length_inc
    else:
        current_length_inc = 1
    if sequence[i] < sequence[i - 1]:
        current_length_dec += 1
        if current_length_dec > max_length_decreasing:
            max_length_decreasing = current_length_dec
    else:
        current_length_dec = 1
print("Наибольшая длина возрастающего фрагмента:", max_length_increasing)
print("Наибольшая длина убывающего фрагмента:", max_length_decreasing)
#b
sequence = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
max_length_increasing = 1
max_length_decreasing = 1
current_length_inc = 1
current_length_dec = 1
for i in range(1, len(sequence)):
    if sequence[i] > sequence[i - 1]:
        current_length_inc += 1
        if current_length_inc > max_length_increasing:
            max_length_increasing = current_length_inc
    else:
        current_length_inc = 1

    if sequence[i] < sequence[i - 1]:
        current_length_dec += 1
        if current_length_dec > max_length_decreasing:
            max_length_decreasing = current_length_dec
    else:
        current_length_dec = 1
print("Наибольшая длина возрастающего фрагмента:", max_length_increasing)
print("Наибольшая длина убывающего фрагмента:", max_length_decreasing)

#7.157
n = int(input("Введите количество чисел: "))
a = []
for _ in range(n):
    a.append(int(input("Введите число: ")))
max_value = a[0]
min_value = a[0]
max_index = 0
min_index = 0
for i in range(n):
    if a[i] >= max_value:
        max_value = a[i]
        max_index = i
    if a[i] <= min_value:
        min_value = a[i]
        min_index = i
print("Номер последнего максимального элемента:", max_index + 1)
print("Номер первого минимального элемента:", min_index + 1)

#7.158
m = int(input("Введите количество чисел: "))
d = []
for _ in range(m):
    d.append(int(input("Введите число: ")))
max_value = d[0]
min_value = d[0]
max_index = 0
min_index = 0
for i in range(m):
    if d[i] >= max_value:
        max_value = d[i]
        max_index = i
    if d[i] <= min_value:
        min_value = d[i]
        min_index = i
print("Номер последнего максимального числа:", max_index + 1)
print("Номер последнего минимального числа:", min_index + 1)

#7.159
n = int(input("Введите количество квартир: "))
residents = []
for i in range(n):
    count = int(input(f"Введите число жильцов в квартире {i+1}: "))
    residents.append(count)
max_residents = residents[0]
apartment_number = 1
for i in range(1, n):
    if residents[i] >= max_residents:
        max_residents = residents[i]
        apartment_number = i + 1
print("Квартира с наибольшим числом жильцов:", apartment_number)

#7.160
n = int(input("Введите количество участников: "))
results = []
for _ in range(n):
    time = float(input("Введите время участника: "))
    results.append(time)
best_time = results[0]
best_index = 0
for i in range(1, n):
    if results[i] < best_time:
        best_time = results[i]
        best_index = i
print("Порядковый номер спортсмена с лучшим результатом:", best_index + 1)

#7.161
n = int(input("Введите количество команд: "))
scores = []
for _ in range(n):
    score = int(input("Введите количество очков команды: "))
    scores.append(score)
min_score = scores[0]
min_index = 0
for i in range(1, n):
    if scores[i] <= min_score:
        min_score = scores[i]
        min_index = i
print("Номер команды с минимальным количеством очков:", min_index + 1)

#7.162
n = int(input("Введите количество дней: "))
precipitations = list(map(float, input("Введите осадки за каждый день через пробел: ").split()))
max_precip = precipitations[0]
max_day = 1
for i in range(1, n):
    if precipitations[i] >= max_precip:
        max_precip = precipitations[i]
        max_day = i + 1  # номерация с 1
print("День с максимальными осадками:", max_day)

#7.163
n = int(input("Введите число покупателей: "))
t = list(map(float, input("Введите времена обслуживания для каждого покупателя: ").split()))
c = [0] * n
min_time = t[0]
min_index = 0
for i in range(n):
    if i == 0:
        c[i] = t[i]
    else:
        c[i] = c[i-1] + t[i]
    if t[i] <= min_time:
        min_time = t[i]
        min_index = i
print("Время пребывания каждого покупателя:", c)
print("Номер покупателя, для которого затрачено минимальное время:", min_index + 1)

#7.164
n = int(input("Введите количество пар: "))
pairs = [tuple(map(float, input(f"Пара {i+1} (a, b): ").split())) for i in range(n)]
max_avg = (pairs[0][0] + pairs[0][1]) / 2
max_avg_index = 0
import math
min_g = math.sqrt(pairs[0][0] * pairs[0][1])
min_g_index = 0
for i in range(1, n):
    a, b = pairs[i]
    avg = (a + b) / 2
    g = math.sqrt(a * b)
    if avg >= max_avg:
        max_avg = avg
        max_avg_index = i
    if g <= min_g:
        min_g = g
        min_g_index = i
print("Номер пары с максимальным средним арифметическим:", max_avg_index + 1)
print("Номер пары с минимальным средним геометрическим:", min_g_index + 1)

#7.165
n = 25
distances = list(map(float, input("Введите длины участков (км): ").split()))
times = list(map(float, input("Введите время в часах: ").split()))
max_speed = 0
max_index = 0
for i in range(n):
    speed = distances[i] / times[i]
    if speed > max_speed:
        max_speed = speed
        max_index = i
print("Номер автомобиля с максимальной средней скоростью:", max_index + 1)

#7.166
n = 20
volts = list(map(float, input("Ввод напряжений (В): ").split()))
resistances = list(map(float, input("Введите сопротивления (Ω): ").split()))
min_current = volts[0] / resistances[0]
min_index = 0
for i in range(1, n):
    current = volts[i] / resistances[i]
    if current < min_current:
        min_current = current
        min_index = i
print("Порядковый номер сопротивления с минимальным током:", min_index + 1)

#7.167
n = int(input("Введите число элементов: "))
x = list(map(int, input("Введите последовательность: ").split()))
max_value = max(x)
min_value = min(x)
first_max_index = x.index(max_value)
first_min_index = x.index(min_value)
if first_max_index < first_min_index:
    print("Максимальное число встречается раньше")
else:
    print("Минимальное число встречается раньше")

#7.168
ages = list(map(int, input("Введите возраст группы: ").split()))
max_age = max(ages)
min_age = min(ages)
first_max_index = ages.index(max_age)
first_min_index = ages.index(min_age)
if first_max_index < first_min_index:
    print("Самый старший встречается раньше")
else:
    print("Самый молодой встречается раньше")

#7.169
times = list(map(float, input("Введите времена на этапах, разделённые пробелом: ").split()))
min_time = min(times)
max_time = max(times)
first_place_index = times.index(min_time) + 1
last_place_index = times.index(max_time) + 1
if first_place_index < last_place_index:
    print("Этап, который он выиграл, был раньше этапа, на котором он занял последнее место.")
else:
    print("Этап, который он выиграл, не был раньше этапа, на котором он занял последнее место.")

#7.170
x = list(map(int, input("Введите последовательность целых чисел через пробел: ").split()))
n = len(x)

# а) максимальная сумма двух соседних чисел
max_sum = x[0] + x[1]
max_sum_pos = 1
for i in range(1, n - 1):
    s = x[i] + x[i + 1]
    if s > max_sum:
        max_sum = s
        max_sum_pos = i + 1

# б) минимальная сумма двух соседних чисел
min_sum = x[0] + x[1]
min_sum_pos = 1
for i in range(1, n - 1):
    s = x[i] + x[i + 1]
    if s < min_sum:
        min_sum = s
        min_sum_pos = i + 1
print(f"Максимальная сумма двух соседних чисел: {max_sum} (позиции: {max_sum_pos} и {max_sum_pos + 1})")
print(f"Минимальная сумма двух соседних чисел: {min_sum} (позиции: {min_sum_pos} и {min_sum_pos + 1})")
print(f"Пар, сумма которых максимальна, первая: позиции {max_sum_pos} и {max_sum_pos + 1}")
print(f"Пар, сумма которых минимальна, последняя: позиции {min_sum_pos} и {min_sum_pos + 1}")

#7.171
x = list(map(int, input("Введите последовательность целых чисел через пробел: ").split()))
max1, max2 = float('-inf'), float('-inf')
for num in x:
    if num > max1:
        max2 = max1
        max1 = num
    elif max1 > num > max2:
        max2 = num
min1, min2 = float('inf'), float('inf')
for num in x:
    if num < min1:
        min2 = min1
        min1 = num
    elif min1 < num < min2:
        min2 = num
print(f"Два максимальных элемента: {max1} и {max2}")
print(f"Два минимальных элемента: {min1} и {min2}")

#7.172
results = list(map(float, input("Введите результаты 22 спортсменов через пробел: ").split()))
min_time = float('inf')
second_min_time = float('inf')
for r in results:
    if r < min_time:
        second_min_time = min_time
        min_time = r
    elif min_time < r < second_min_time:
        second_min_time = r
first_place_index = results.index(min_time) + 1
second_place_index = results.index(second_min_time) + 1
print(f"Первое место: спортсмен {first_place_index} с результатом {min_time}")
print(f"Второе место: спортсмен {second_place_index} с результатом {second_min_time}")

#7.173
speeds = list(map(float, input("Введите максимальные скорости 12 марок автомобилей через пробел: ").split()))
max_speed = max(speeds)
filtered_speeds = [s for s in speeds if s < max_speed]
if filtered_speeds:
    speed_bigger_than_only_max = max(filtered_speeds)
    print(f"Скорость автомобиля, больше которой только максимальное значение: {speed_bigger_than_only_max}")
else:
    print("Все автомобили имеют одинаковую максимальную скорость.")