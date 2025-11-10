#7.18
n = int(input("Введите n: "))
x = list(map(int, input("Введите числа xi через пробел: ").split()))
b = int(input("Введите b: "))
if sum(x) % b == 0:
    print("Сумма чисел кратна b")
else:
    print("Сумма чисел не кратна b")

#7.19
current_year_precip = float(input("Введите осадков за февраль в текущем году: "))
last_year_precip = float(input("Введите осадков за февраль в прошлом году: "))
if current_year_precip > last_year_precip:
    print("Общее количество осадков за февраль превышает прошлогоднее")
else:
    print("Общее количество осадков за февраль не превышает прошлогоднее")

#7.20
n = int(input("Введите количество грузов: "))
masses = list(map(float, input("Введите массы грузов через пробел: ").split()))
car_capacity = float(input("Введите грузоподъемность автомобиля: "))
if sum(masses) <= car_capacity:
    print("Общая масса не превышает грузоподъемность автомобиля")
else:
    print("Общая масса превышает грузоподъемность автомобиля")

#7.21
scores1 = list(map(int, input("Введите результаты первого спортсмена через пробел: ").split()))
scores2 = list(map(int, input("Введите результаты второго спортсмена через пробел: ").split()))
sum1 = sum(scores1)
sum2 = sum(scores2)
if sum1 > sum2:
    print("Первый спортсмен показал лучший результат")
elif sum2 > sum1:
    print("Второй спортсмен показал лучший результат")
else:
    print("Результаты равны")

#7.22
set1 = list(map(float, input("Введите стоимости предметов первого набора: ").split()))
set2 = list(map(float, input("Введите стоимости предметов второго набора: ").split()))
cost1 = sum(set1)
cost2 = sum(set2)
if cost1 < cost2:
    print("Первый набор дешевле")
elif cost2 < cost1:
    print("Второй набор дешевле")
else:
    print("Оба набора стоят одинаково")

#7.23
a = list(map(int, input("Введите 8 чисел через пробел: ").split()))
product = 1
for num in a:
    product *= num
print("Меньше 10000:", product < 10000)

#7.24
n = int(input("Введите n: "))
d = list(map(float, input("Введите числа через пробел: ").split()))
s = float(input("Введите s: "))
product = 1
for num in d:
    product *= num
print("Произведение больше s:", product > s)

#7.25
a = list(map(float, input("Введите 10 чисел через пробел: ").split()))
average = sum(a) / 10
print("Среднее арифметическое:", average)

#7.26
n = int(input("Введите n: "))
a = list(map(float, input(f"Введите {n} чисел через пробел: ").split()))
average = sum(a) / n
print("Среднее арифметическое:", average)

#7.27
ratings = list(map(int, input("Введите оценки 20 учеников через пробел: ").split()))
average = sum(ratings) / 20
print("Средняя оценка:", average)

#7.28
grades = list(map(int, input("Введите оценки по 10 предметам: ").split()))
average = sum(grades) / 10
print("Средняя оценка:", average)

#7.29
grades = list(map(int, input("Введите оценки по алгебре учеников через пробел: ").split()))
average = sum(grades) / len(grades)
print("Средняя оценка по алгебре:", average)

#7.30
masses = list(map(float, input("Введите массы предметов: ").split()))
average = sum(masses) / len(masses)
print("Средняя масса:", average)

#7.31
numbers = []
while True:
    num = int(input())
    if num < 0:
        break
    numbers.append(num)
if numbers:
    print("Среднее арифметическое:", sum(numbers) / len(numbers))
else:
    print("Последовательность пуста")

#7.32
ages_class1 = list(map(float, input("Введите возраст 20 учеников первого класса: ").split()))
ages_class2 = list(map(float, input("Введите возраст 20 учеников второго класса: ").split()))
avg1 = sum(ages_class1) / 20
avg2 = sum(ages_class2) / 20
print("Средний возраст первого класса:", avg1)
print("Средний возраст второго класса:", avg2)

#7.33
precip_january = list(map(float, input("Введите осадки за каждый январдый день: ").split()))
precip_march = list(map(float, input("Введите осадки за каждый мартовский день: ").split()))
avg_january = sum(precip_january) / len(precip_january)
avg_march = sum(precip_march) / len(precip_march)
print("Среднедневные осадки за январь:", avg_january)
print("Среднедневные осадки за март:", avg_march)

#7.34
growth_class1 = list(map(float, input("Введите рост учеников первого класса: ").split()))
growth_class2 = list(map(float, input("Введите рост учеников второго класса: ").split()))
avg1 = sum(growth_class1) / len(growth_class1)
avg2 = sum(growth_class2) / len(growth_class2)
print("Средний рост первого класса:", avg1)
print("Средний рост второго класса:", avg2)

#7.35
class1 = list(map(float, input("Введите оценки 1 класса через пробел: ").split()))
class2 = list(map(float, input("Введите оценки 2 класса через пробел: ").split()))
avg_class1 = sum(class1) / len(class1)
avg_class2 = sum(class2) / len(class2)
print(f"Средняя оценка 1 класса: {avg_class1}")
print(f"Средняя оценка 2 класса: {avg_class2}")

#7.36
areas = list(map(float, input("Введите площади районов через пробел: ").split()))
yields = list(map(float, input("Введите урожайность районов: ").split()))
total_wheat = sum(area * yield_ for area, yield_ in zip(areas, yields))
average_yield = sum(yields) / len(yields)
print(f"Общее количество пшеницы: {total_wheat} ц")
print(f"Средняя урожайность: {average_yield} ц/га")

#7.37
populations = list(map(float, input("Введите численность жителей районов (тыс. человек): ").split()))
areas = list(map(float, input("Введите площади районов (км^2): ").split()))
total_population = sum(populations)
total_area = sum(areas)
density = total_population / total_area
print(f"Средняя плотность населения: {density} тыс. чел./км^2")

#7.38
populations = list(map(float, input("Введите численность жителей (тыс. человек): ").split()))
densities = list(map(float, input("Введите плотность населения в районах (тыс. чел./км^2): ").split()))
total_area = 0
for p, d in zip(populations, densities):
    area = p / d
    total_area += area
print(f"Общая площадь области: {total_area} км^2")

#7.39
n = int(input("Введите n: "))
a = list(map(int, input(f"Введите {n} чисел через пробел: ").split()))

# а
sum_abs = sum(abs(x) for x in a)

# б
prod_abs = 1
for x in a:
    prod_abs *= abs(x)

# в
adjacent_sums = [a[i] + a[i+1] for i in range(n-1)]

# г
alt_sum = 0
for i in range(n):
    if i % 2 == 0:
        alt_sum += a[i]
    else:
        alt_sum -= a[i]
print(f"а) сумма модулей: {sum_abs}")
print(f"б) произведение модулей: {prod_abs}")
print(f"в) суммы соседних элементов: {adjacent_sums}")
print(f"г) чередующаяся сумма: {alt_sum}")

#7.40
numbers = [float(input(f"Введите число {i+1}: ")) for i in range(12)]
result = sum(x for x in numbers if x > 10.75)
print(f"Сумма чисел больше 10.75: {result}")

#7.41
n = int(input("Введите n: "))
p = float(input("Введите значение p: "))
b = [float(input(f"b[{i+1}]=")) for i in range(n)]
result = sum(x for x in b if x > p)
print(f"Сумма чисел больше {p}: {result}")

#7.42
d = [int(input(f"d[{i+1}]=")) for i in range(10)]
result = sum(x for x in d if x % 2 == 0)
print(f"Сумма четных чисел: {result}")

#7.43
numbers = [int(input(f"Число {i+1}: ")) for i in range(10)]
result = sum(x for x in numbers if x % 10 == 0)
print(f"Сумма чисел, оканчивающихся нулем: {result}")

#7.44
a = list(map(int, input("Введите 20 чисел через пробел: ").split()))
sum_even_indices = sum(a[i] for i in range(1, 20, 2))
print(f"Сумма элементов с четными номерами: {sum_even_indices}")

#7.45
c = list(map(float, input("Введите 15 чисел через пробел: ").split()))
result = -sum(c[i] for i in range(0, 15, 2))
print(f"Результат: {result}")

#7.46
n = int(input("Введите n: "))
a = list(map(int, input(f"Введите {n} чисел: ").split()))
first_last = a[0] + a[-1]
second_penultimate = a[1] - a[-2]
print(f"Сумма первого и последнего: {first_last}")
print(f"Разность второго и предпоследнего: {second_penultimate}")

#7.47
n = int(input("Введите количество товаров: "))
costs = [float(input(f"Стоимость товара {i+1}: ")) for i in range(n)]
total = sum(cost for cost in costs if cost > 1000)
print(f"Общая стоимость товаров дороже 1000: {total}")

#7.48
n = int(input("Введите число журналов: "))
total_pages = 0
for i in range(n):
    pages = int(input(f"Число страниц журнала {i+1}: "))
    total_pages += pages
print(f"Общее число страниц во всех журналах: {total_pages}")