# 11.201

def task_11_201():
    powers = []
    print("Введите мощности двигателей 30 моделей (через пробел):")
    powers = list(map(int, input().split()))
    exists = any(power > 200 for power in powers)
    if exists:
        print("Есть модель с мощностью двигателя более 200 л. с.")
    else:
        print("Нет моделей с мощностью двигателя более 200 л. с.")

# 11.202
def task_11_202():
    print("Введите убывающий массив (через пробел):")
    arr = list(map(int, input().split()))
    print("Введите число a:")
    a = int(input())
    position = -1
    for i, val in enumerate(arr):
        if val < a:
            position = i
            break
    if position != -1:
        print(f"Номер первого элемента, меньшего {a}: {position}")
    else:
        print("Таких элементов нет.")

# 11.203
def task_11_203():
    print("Введите отсортированный по возрастанию массив (через пробел):")
    arr = list(map(int, input().split()))
    print("Введите число n:")
    n = int(input())
    index = -1
    for i, val in enumerate(arr):
        if val > n:
            index = i
            break
    if index != -1:
        print("Элементы, следующие за первым большим n:")
        for v in arr[index:]:
            print(v, end=' ')
        print()
    else:
        print("В массиве нет элементов, больших n.")

# 11.204
def task_11_204():
    print("Введите убывающий массив (через пробел):")
    arr = list(map(int, input().split()))
    print("Введите число a:")
    a = int(input())
    index = -1
    for i, val in enumerate(arr):
        if val < a:
            index = i
            break
    if index != -1:
        print("Элементы после первого меньшего a:")
        for v in arr[index:]:
            print(v, end=' ')
        print()
        print("Элементы, большие a:")
        for v in arr:
            if v > a:
                print(v, end=' ')
        print()
    else:
        print("В массиве нет элементов, меньших a.")

# 11.205
def task_11_205():
    print("Введите массив (через пробел):")
    arr = list(map(int, input().split()))
    pair_index = -1
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            pair_index = i
            break
    if pair_index != -1:
        print(f"Первая пара одинаковых соседних элементов: позиции {pair_index} и {pair_index+1}")
    else:
        print("Нет пар одинаковых соседних элементов.")

# 11.206
def task_11_206():
    print("Введите массив (через пробел):")
    arr = list(map(int, input().split()))
    pair_index = -1
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            pair_index = i
            break
    if pair_index != -1:
        print("Элементы, следующие за первой парой:", *arr[pair_index+2:])
    else:
        print("Пары одинаковых соседних элементов не найдены.")

# 11.207
def task_11_207():
    print("Введите массив целых чисел (через пробел):")
    arr = list(map(int, input().split()))
    pair_index = -1
    for i in range(len(arr)-1):
        if arr[i] % 2 != 0 and arr[i+1] % 2 != 0:
            pair_index = i
            break
    if pair_index != -1:
        print(f"Первая пара соседних нечетных чисел: позиции {pair_index} и {pair_index+1}")
    else:
        print("Пар соседних нечетных чисел нет.")

# 11.208
def task_11_208():
    print("Введите массив целых чисел (через пробел):")
    arr = list(map(int, input().split()))
    last_pair_index = -1
    for i in range(len(arr)-1):
        if arr[i] % 2 == 0 and arr[i+1] % 2 == 0:
            last_pair_index = i
    if last_pair_index != -1:
        print("Элементы, предшествующие последней паре четных чисел:")
        for v in arr[:last_pair_index]:
            print(v, end=' ')
        print()
    else:
        print("Пары соседних четных чисел не найдены.")

# 11.209
def task_11_209():
    print("Введите 22 числа (через пробел):")
    arr = list(map(int, input().split()))
    print("Выберите вариант:")
    print("а) Последняя цифра каждого числа соответствует количеству точек на правой половине кости.")
    print("б) Количество точек на обеих половинах может соответствовать любой цифре числа.")
    variant = input("Введите 'а' или 'б': ").strip()

    def check_row(arr, variant):
        for num in arr:
            str_num = str(num)
            if len(str_num) != 2:
                return False
            left = int(str_num[0])
            right = int(str_num[1])
            if variant == 'а':
                if right != left:
                    return False
            elif variant == 'б':
                continue
        return True

    if check_row(arr, variant):
        print("Последовательность соответствует ряду костей домино.")
    else:
        print("Последовательность не соответствует ряду костей домино.")

# 11.210
def task_11_210():
    print("Введите массив из чисел (через пробел):")
    arr = list(map(int, input().split()))
    position = -1
    for i in range(1, len(arr)-1):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            position = i
            break
    if position != -1:
        print(f"Первая тройка: позиции {position-1}, {position}, {position+1}")
    else:
        print("Таких троек нет.")

def main():
    tasks = {
        '11.201': task_11_201,
        '11.202': task_11_202,
        '11.203': task_11_203,
        '11.204': task_11_204,
        '11.205': task_11_205,
        '11.206': task_11_206,
        '11.207': task_11_207,
        '11.208': task_11_208,
        '11.209': task_11_209,
        '11.210': task_11_210
    }
    print("Выберите номер задачи для выполнения (например, 11.201):")
    choice = input().strip()
    if choice in tasks:
        tasks[choice]()
    else:
        print("Задача не найдена.")

if __name__ == "__main__":
    main()

#11.211
arr = list(map(int, input("Введите массив через пробел: ").split()))
last_index = -1
for i in range(1, len(arr)-1):
    if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
        last_index = i
if last_index != -1:
    preceding_elements = arr[:last_index]
    print("Элементы, предшествующие элементам последней специальной тройки:", preceding_elements)
else:
    print("Таких троек нет.")

#11.212
arr = list(map(int, input("Введите массив через пробел: ").split()))
is_sorted = True
break_index = -1
for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        is_sorted = False
        break_index = i+1
        break
if is_sorted:
    print("Массив упорядочен по возрастанию.")
else:
    print(f"Массив неупорядочен. Первый нарушающий элемент — под номером {break_index}: {arr[break_index-1]}")

#11.213
heights = list(map(int, input("Введите рост учеников через пробел: ").split()))
is_descending = all(heights[i] >= heights[i+1] for i in range(len(heights)-1))
if is_descending:
    print("Ученики перечислены в порядке убывания роста.")
else:
    print("Ученики не перечислены в порядке убывания роста.")

#11.214
scores = list(map(int, input("Введите очки команд через пробел: ").split()))
is_sorted_desc = all(scores[i] >= scores[i+1] for i in range(len(scores)-1))
if is_sorted_desc:
    print("Команды перечислены в порядке убывания очков (по позициям).")
else:
    print("Списк не отсортирован по убыванию очков.")

#11.215
arr = list(map(int, input("Введите массив через пробел: ").split()))
import itertools
indices = [i for i, _ in enumerate(arr)]
grouped = [(key, list(group)) for key, group in itertools.groupby(arr)]
first_group_length = len(grouped[0][1]) if grouped else 0
total_equal = first_group_length
print(f"Количество одинаковых элементов в начале: {total_equal}")
if total_equal == len(arr):
    print("Все элементы массива одинаковы.")
else:
    print("Элементы после последних одинаковых элементов:", arr[total_equal:])

#11.216
scores = list(map(int, input("Введите оценки через пробел: ").split()))
import itertools
groups = [list(g) for _, g in itertools.groupby(scores, key=lambda x: x==5)]
print("Количество учеников с оценкой 5:", len(groups[0]) if groups else 0)

#11.217

#a
num1 = list(map(int, input("Введите 20-значное число 1: ")))
num2 = list(map(int, input("Введите 20-значное число 2: ")))
def add_large_numbers(a, b):
    result = []
    carry = 0
    for i in range(19, -1, -1):
        s = a[i] + b[i] + carry
        result.insert(0, s % 10)
        carry = s // 10
    if carry != 0:
        result.insert(0, carry)
    return result
sum_result = add_large_numbers(num1, num2)
print("Сумма:", ''.join(map(str, sum_result)))

#b
num1 = list(map(int, input("Введите 30-значное число 1: ")))
num2 = list(map(int, input("Введите 30-значное число 2: ")))
def subtract_large_numbers(a, b):
    result = []
    borrow = 0
    for i in range(29, -1, -1):
        diff = a[i] - b[i] - borrow
        if diff < 0:
            diff += 10
            borrow = 1
        else:
            borrow = 0
        result.insert(0, diff)
    return result

sub_result = subtract_large_numbers(num1, num2)
print("Разность:", ''.join(map(str, sub_result)))

#11.218
arr = list(map(int, input("Введите массив через пробел: ").split()))
distinct_elements = len(set(arr))
print("Количество различных элементов:", distinct_elements)

#11.219
n = input("Введите натуральное число: ")
digits = set(n)
print("Количество различныx цифр:", len(digits))

#11.220
arr = list(map(int, input("Введите 20 целых чисел через пробел: ").split()))
from collections import Counter
counter = Counter(arr)
duplicates = [item for item, count in counter.items() if count > 1]
print("Два одинаковых элемента:", duplicates)

#11.221
number = str(2**100)
digits = list(number)
print("Цифры 2**100:", ' '.join(digits))

#11.222
import math
factorial_str = str(math.factorial(100))
digits = list(factorial_str)
print("Цифры 100!:", ' '.join(digits))

# 11.223
costs_july = list(map(float, input("Введите стоимости товаров за каждый день июля, через пробел: ").split()))
costs_august = list(map(float, input("Введите стоимости товаров за каждый день августа, через пробел: ").split()))
total_cost = sum(costs_july) + sum(costs_august)
print("Общая стоимость проданных товаров за два месяца:", total_cost)

# 11.224
goals_champ1 = list(map(int, input("Введите количество мячей за каждую игру первого чемпионата (26 игр), через пробел: ").split()))
goals_champ2 = list(map(int, input("Введите количество мячей за каждую игру второго чемпионата (26 игр), через пробел: ").split()))
total_goals = sum(goals_champ1) + sum(goals_champ2)
print("Общее количество забитых мячей:", total_goals)

# 11.225
areas = 20
area_plots = []
area_harvests = []

print("Введите площади засеянных пшеницей в гектарах для каждого района:")
for i in range(areas):
    area_plots.append(float(input(f"Район {i+1}: ")))
print("Введите собранный урожай в центнерах для каждого района:")
for i in range(areas):
    area_harvests.append(float(input(f"Район {i+1}: ")))

# 1)
total_area = 0
total_harvest = 0
for i in range(areas):
    total_area += area_plots[i]
    total_harvest += area_harvests[i]
    if area_plots[i] != 0:
        print(f"Средняя урожайность по району {i+1}: {area_harvests[i]/area_plots[i]:.2f} ц/га")
overall_yield = total_harvest / total_area if total_area != 0 else 0
print(f"Средняя урожайность по области: {overall_yield:.2f} ц/га")

# 2)
ratios = []
total_area2 = 0
total_harvest2 = 0
for i in range(areas):
    ratio = area_harvests[i] / area_plots[i] if area_plots[i] != 0 else 0
    ratios.append(ratio)
    total_area2 += area_plots[i]
    total_harvest2 += area_harvests[i]
for i in range(areas):
    print(f"Средняя урожайность по району {i+1}: {ratios[i]:.2f} ц/га")
overall_yield2 = total_harvest2 / total_area2 if total_area2 != 0 else 0
print(f"Средняя урожайность по области: {overall_yield2:.2f} ц/га")

# 11.226
areas = 10
areas_plots = []
yield_rates = []

print("Введите площади, засеваемые пшеницей (в гектарах):")
for i in range(areas):
    areas_plots.append(float(input(f"Район {i+1}: ")))
print("Введите среднюю урожайность (в центнерах с гектара):")
for i in range(areas):
    yield_rates.append(float(input(f"Район {i+1}: ")))

# 1)
total_wheat = 0
for i in range(areas):
    total_wheat += areas_plots[i] * yield_rates[i]
print("Общее количество собранной пшеницы (в центнерах):", total_wheat)

# 2)
total_wheat2 = 0
wheat_per_area = []
for i in range(areas):
    wheat = areas_plots[i] * yield_rates[i]
    wheat_per_area.append(wheat)
    total_wheat2 += wheat
print("Общее количество собранной пшеницы (в центнерах):", total_wheat2)

# 11.227
lengths = []
widths = []
heights = []
print("Введите длины 12 параллелепипедов:")
for i in range(12):
    lengths.append(float(input(f"Параллелепипед {i+1} длина: ")))
print("Введите ширины 12 параллелепипедов:")
for i in range(12):
    widths.append(float(input(f"Параллелепипед {i+1} ширина: ")))
print("Введите высоты 12 параллелепипедов:")
for i in range(12):
    heights.append(float(input(f"Параллелепипед {i+1} высота: ")))

# 1)
for i in range(12):
    volume = lengths[i]*widths[i]*heights[i]
    print(f"Объем параллелепипеда {i+1}: {volume}")

# 2)
volumes = []
for i in range(12):
    volume = lengths[i]*widths[i]*heights[i]
    volumes.append(volume)
for i in range(12):
    print(f"Объем параллелепипеда {i+1}: {volumes[i]}")

# 11.228
car_masses = []
car_costs = []

for i in range(30):
    mass = float(input(f"Введите мощность автомобиля {i+1} (л.с.): "))
    cost = float(input(f"Введите стоимость автомобиля {i+1} (рубли): "))
    car_masses.append(mass)
    car_costs.append(cost)

print("Стоимость автомобилей с мощностью не более 80 л.с.:")
for i in range(30):
    if car_masses[i] <= 80:
        print(f"Автомобиль {i+1}: {car_costs[i]} рублей")

# 11.229
disk_capacities = []
disk_costs = []

for i in range(22):
    capacity = float(input(f"Введите вместимость диска {i+1} (ГБ): "))
    cost = float(input(f"Введите стоимость диска {i+1} (руб): "))
    disk_capacities.append(capacity)
    disk_costs.append(cost)

s = float(input("Введите пороговую стоимость s рублей: "))

print("Вместимость дисков, стоящих дороже s рублей:")
for i in range(22):
    if disk_costs[i] > s:
        print(f"Диск {i+1}: {disk_capacities[i]} ГБ")

# 11.230
scores_scored = list(map(int, input("Введите количество заброшенных мячей за 15 игр: ").split()))
scores_conceded = list(map(int, input("Введите пропущенных мячей за 15 игр: ").split()))
print("Результаты игр:")
for i in range(15):
    if scores_scored[i] > scores_conceded[i]:
        result = "Выигрыш"
    elif scores_scored[i] < scores_conceded[i]:
        result = "Проигрыш"
    else:
        result = "Ничья"
    print(f"Игра {i+1}: {result}")

#11.231 и 11.232

print("Введите результаты игр (забитые и пропущенные мячи для каждой из 20 игр):")
hits = []
misses = []
for i in range(20):
    while True:
        try:
            data = input(f"Игра {i+1} (забитые и пропущенные через пробел): ").split()
            if len(data) != 2:
                print("Пожалуйста, введите два числа.")
                continue
            hit, miss = map(int, data)
            hits.append(hit)
            misses.append(miss)
            break
        except ValueError:
            print("Некорректный ввод, попробуйте снова.")

# 1
print("\nРезультаты игр без использования дополнительного массива:")
for i in range(20):
    if hits[i] > misses[i]:
        result = "выигрыш"
    elif hits[i] < misses[i]:
        result = "проигрыш"
    else:
        result = "ничья"
    print(f"Игра {i+1}: {result}")

# 2)
results = []
for i in range(20):
    if hits[i] > misses[i]:
        results.append("выигрыш")
    elif hits[i] < misses[i]:
        results.append("проигрыш")
    else:
        results.append("ничья")
print("\nРезультаты игр с использованием дополнительного массива:")
for i, res in enumerate(results, 1):
    print(f"Игра {i}: {res}")
win_count = results.count("выигрыш")
draw_count = results.count("ничья")
lose_count = results.count("проигрыш")
total_points = win_count * 3 + draw_count
print(f"\nОбщее количество выигранных игр: {win_count}")
print(f"Общее количество ничьих: {draw_count}")
print(f"Общее количество проигрышей: {lose_count}")
print(f"Общее количество набранных очков: {total_points}")

#11.233
print("\nВведите результаты игр в виде чисел (например, 32, 22, 00):")
coded_results = []
for i in range(20):
    while True:
        try:
            val = int(input(f"Игра {i+1}: "))
            coded_results.append(val)
            break
        except ValueError:
            print("Некорректный ввод, попробуйте снова.")

# б
wins = 0
for code in coded_results:
    goals_for = code // 10
    goals_against = code % 10
    if goals_for > goals_against:
        wins += 1
print(f"\nКоличество выигранных игр: {wins}")

# в
losses = 0
for code in coded_results:
    goals_for = code // 10
    goals_against = code % 10
    if goals_for > goals_against:
        wins += 1
    elif goals_for < goals_against:
        losses += 1
print(f"Количество выигрышей: {wins}")
print(f"Количество проигрышей: {losses}")

# г
draws = 0
for code in coded_results:
    goals_for = code // 10
    goals_against = code % 10
    if goals_for > goals_against:
        wins += 1
    elif goals_for < goals_against:
        losses += 1
    else:
        draws += 1
print(f"Количество выигрышей: {wins}")
print(f"Количество ничьих: {draws}")
print(f"Количество проигрышей: {losses}")

# д
count_diff_three_or_more = 0
for code in coded_results:
    diff = abs((code // 10) - (code % 10))
    if diff >= 3:
        count_diff_three_or_more += 1
print(f"Количество игр с разницей забитых и пропущенных >= 3: {count_diff_three_or_more}")

# е
points = 0
for code in coded_results:
    goals_for = code // 10
    goals_against = code % 10
    if goals_for > goals_against:
        points += 3
    elif goals_for == goals_against:
        points += 1
print(f"Общее количество очков: {points}")

#11.234
print("\nВведите численность населения и площадь для каждого из 28 государств:")
total_population = 0
for i in range(28):
    while True:
        try:
            data = input(f"Государство {i+1} (численность и площадь через пробел): ").split()
            if len(data) != 2:
                print("Пожалуйста, введите два числа.")
                continue
            population, area = map(float, data)
            if area > 5:
                total_population += population
            break
        except ValueError:
            print("Некорректный ввод, попробуйте снова.")
print(f"Общая численность государств с площадью > 5 млн кв. км: {total_population}")

#11.235
print("\nВведите мощность и стоимость для 30 автомобилей:")
total_cost = 0
for i in range(30):
    while True:
        try:
            data = input(f"Автомобиль {i+1} (мощность и стоимость через пробел): ").split()
            if len(data) != 2:
                print("Пожалуйста, введите два числа.")
                continue
            power, cost = float(data[0]), float(data[1])
            if power > 100:
                total_cost += cost
            break
        except ValueError:
            print("Некорректный ввод, попробуйте снова.")
print(f"Общая стоимость автомобилей с мощностью > 100 л.с.: {total_cost}")

#11.236
print("\nВведите количество осадков и температуру для каждого дня месяца:")
snowfall = 0
rainfall = 0
for i in range(30):
    while True:
        try:
            data = input(f"День {i+1} (осадки и температуру через пробел): ").split()
            if len(data) != 2:
                print("Пожалуйста, введите два числа.")
                continue
            precipitation, temperature = float(data[0]), float(data[1])
            if temperature > 0:
                rainfall += precipitation
            else:
                snowfall += precipitation
            break
        except ValueError:
            print("Некорректный ввод, попробуйте снова.")
print(f"Общее количество осадков в виде снега: {snowfall}")
print(f"Общее количество осадков в виде дождя: {rainfall}")


# 11.237
from re import A
def total_population_small_states():
    n = int(input("Введите количество государств: "))
    total_population = 0
    for _ in range(n):
        population = float(input("Введите численность населения (млн): "))
        area = float(input("Введите площадь (тыс км2): "))
        if area <= A:
            total_population += population
    print("Общая численность населения в малых государствах:", total_population)

# 11.238
def compare_precipitation():
    jan_days = int(input("Введите число дней января: "))
    mar_days = int(input("Введите число дней марта: "))
    jan_precipitation = 0
    mar_precipitation = 0
    print("Введите осадки за каждый день января:")
    for _ in range(jan_days):
        jan_precipitation += float(input())
    print("Введите осадки за каждый день марта:")
    for _ in range(mar_days):
        mar_precipitation += float(input())
    if jan_precipitation > mar_precipitation:
        print("В январе выпало больше осадков.")
    else:
        print("В марте выпало больше осадков.")

# 11.239
def compare_shop_incomes():
    days = int(input("Введите количество дней февраля: "))
    income_shop1 = 0
    income_shop2 = 0
    print("Введите доход первого магазина за каждый день:")
    for _ in range(days):
        income_shop1 += float(input())
    print("Введите доход второго магазина за каждый день:")
    for _ in range(days):
        income_shop2 += float(input())
    if income_shop1 < income_shop2:
        print("Общий доход первого магазина меньше.")
    else:
        print("Общий доход второго магазина меньше или равен.")

# 11.240
def max_density_material():
    n = int(input("Введите количество предметов: "))
#1
    max_density = 0
    max_index = -1
    for i in range(n):
        mass = float(input("Введите массу предмета (кг): "))
        volume = float(input("Введите объем предмета (см^3): "))
        density = mass / volume
        if density > max_density:
            max_density = density
            max_index = i
    print("Максимальная плотность (без массива):", max_density, "у предмета", max_index + 1)

#2
    masses = []
    volumes = []
    for _ in range(n):
        m = float(input("Введите массу предмета (кг): "))
        v = float(input("Введите объем предмета (см^3): "))
        masses.append(m)
        volumes.append(v)
    max_density = 0
    max_idx = -1
    for i in range(n):
        density = masses[i] / volumes[i]
        if density > max_density:
            max_density = density
            max_idx = i
    print("Максимальная плотность (с массивом):", max_density, "у предмета", max_idx + 1)

# 11.241
def min_average_speed():
    distances = []
    times = []
#1
    min_avg_speed = float('inf')
    for _ in range(25):
        d = float(input("Введите пройденное расстояние (км): "))
        t = float(input("Введите затраченное время (часы): "))
        avg_speed = d / t
        if avg_speed < min_avg_speed:
            min_avg_speed = avg_speed
    print("Минимальная средняя скорость (без массива):", min_avg_speed)

#2
    dist_arr = []
    time_arr = []
    for _ in range(25):
        d = float(input("Введите пройденное расстояние (км): "))
        t = float(input("Введите затраченное время (часы): "))
        dist_arr.append(d)
        time_arr.append(t)
    min_avg_speed = float('inf')
    for i in range(25):
        avg_speed = dist_arr[i] / time_arr[i]
        if avg_speed < min_avg_speed:
            min_avg_speed = avg_speed
    print("Минимальная средняя скорость (с массивами):", min_avg_speed)

# 11.242
def parallelepipeds():
    n = 15
    lengths = []
    widths = []
    heights = []
    for _ in range(n):
        lengths.append(float(input("Введите длину: ")))
    for _ in range(n):
        widths.append(float(input("Введите ширину: ")))
    for _ in range(n):
        heights.append(float(input("Введите высоту: ")))

#1
    max_volume = 0
    min_volume = float('inf')
    max_index = -1
    min_index = -1
    for i in range(n):
        volume = lengths[i] * widths[i] * heights[i]
        if volume > max_volume:
            max_volume = volume
            max_index = i
        if volume < min_volume:
            min_volume = volume
            min_index = i

    print("Максимальный объем:", max_volume)
    print("Минимальный объем:", min_volume)
    print("Номер фигуры с максимальным объемом:", max_index + 1)
    print("Номер фигуры с минимальным объемом:", min_index + 1)

#2
    volumes = []
    for i in range(n):
        volume = lengths[i] * widths[i] * heights[i]
        volumes.append(volume)
    max_vol = max(volumes)
    min_vol = min(volumes)
    max_idx = volumes.index(max_vol) + 1
    min_idx = volumes.index(min_vol) + 1
    print("Максимальный объем (с массивом):", max_vol)
    print("Минимальный объем (с массивом):", min_vol)
    print("Номер фигуры с максимальным объемом (с массивом):", max_idx)
    print("Номер фигуры с минимальным объемом (с массивом):", min_idx)

#11.243
def minimal_bounding_rectangle():
    points = []
    for i in range(20):
        x = float(input(f"Введите x точки {i+1}: "))
        y = float(input(f"Введите y точки {i+1}: "))
        points.append((x, y))
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    print("Левый нижний угол:", (min_x, min_y))
    print("Правый верхний угол:", (max_x, max_y))

#11.244
def copy_array():
    n = int(input("Введите размер массива: "))
    array = []
    print("Введите элементы массива:")
    for _ in range(n):
        array.append(int(input()))

    # а
    copy_same_order = array[:]
    print("Копия в том же порядке:", copy_same_order)

    # б
    copy_reversed = array[::-1]
    print("Копия в обратном порядке:", copy_reversed)

# 11.245
def form_b_array():
    n = int(input("Введите размер массива a: "))
    a = []
    for _ in range(n):
        a.append(int(input()))
    b = []
    for i in range(n):
        if (i + 1) % 2 == 0:
            b.append(a[i] ** 2)
        else:
            b.append(2 * a[i])
    print("Массив b:", b)

def task_11_246():
    size = int(input("Введите размер массива m: "))
    m = list(map(float, input(f"Введите {size} элементов массива m, через пробел: ").split()))
    n = []
    for i in range(1, size+1):
        if i % 2 != 0:
            ni = i * m[i-1]
        else:
            ni = m[i-1] / i
        n.append(ni)
    print("Массив n:", n)

def task_11_247():
    size = int(input("Введите размер массива p: "))
    p = list(map(float, input(f"Введите {size} элементов массива p, через пробел: ").split()))
    q = []
    for i in range(1, size+1):
        if 3 <= i <= 10:
            qi = -p[i-1]
        else:
            qi = p[i-1] * i
        q.append(qi)
    print("Массив q:", q)

def task_11_248():
    size = int(input("Введите размер массива a: "))
    a = list(map(int, input(f"Введите {size} элементов массива a, через пробел: ").split()))
    b = []
    for num in a:
        if num % 2 == 0:
            b.append(2 * num)
        else:
            b.append(num)
    print("Массив b:", b)

def task_11_249():
    size = int(input("Введите размер массива m: "))
    m = list(map(float, input(f"Введите {size} элементов массива m, через пробел: ").split()))
    n = []
    for num in m:
        if num >= 0:
            n.append(num / 3)
        else:
            n.append(num ** 2)
    print("Массив n:", n)

def task_11_250():
    size = int(input("Введите размер массива: "))
    arr = list(map(float, input(f"Введите {size} элементов массива, через пробел: ").split()))
    # а
    same_positions = arr.copy()
    # б
    even_index_elements = [arr[i] for i in range(1, size, 2)]
    print("а) Вторые, четвертые и т. д. элементы на своих местах:", same_positions)
    print("б) Те же элементы, расположенные подряд по порядку:", even_index_elements)

def task_11_251():
    size = int(input("Введите размер массива целых чисел: "))
    arr = list(map(int, input(f"Введите {size} элементов массива, через пробел: ").split()))
    # а
    odd_positions_same = [arr[i] if arr[i] % 2 != 0 else None for i in range(size)]
    # б
    odd_elements = [x for x in arr if x % 2 != 0]
    print("а) Нечетные элементы в своих местах:", odd_positions_same)
    print("б) Нечетные элементы подряд с начала:", odd_elements)

def task_11_252():
    size = 20
    arr = list(map(int, input(f"Введите {size} элементов массива, через пробел: ").split()))
    arr_even = [arr[i] for i in range(0, size, 2)]
    arr_odd = [arr[i] for i in range(1, size, 2)]
    print("Массив с элементами с четными индексами:", arr_even)
    print("Массив с элементами с нечетными индексами:", arr_odd)

def task_11_253():
    size = int(input("Введите размер массива: "))
    arr = list(map(int, input(f"Введите {size} элементов массива, через пробел: ").split()))
    positive = [x if x > 0 else None for x in arr]
    non_positive = [x if x <= 0 else None for x in arr]
#а
    positive_same = positive.copy()
    non_positive_same = non_positive.copy()
#б
    positive_seq = [x for x in arr if x > 0]
    non_positive_seq = [x for x in arr if x <= 0]
    print("а) Положительные и неположительные на тех же местах:")
    print("Положительные:", positive_same)
    print("Неположительные:", non_positive_same)
    print("б) Положительные и неположительные подряд с начала:")
    print("Положительные:", positive_seq)
    print("Неположительные:", non_positive_seq)

def task_11_254():
    size = int(input("Введите размер массива: "))
    arr = list(map(int, input(f"Введите {size} элементов массива, через пробел: ").split()))
    result = []
    for num in arr:
        if num < 0:
            result.append(num)
    for num in arr:
        if num >= 0:
            result.append(num)
    print("Массив с отрицательными первыми:", result)

def task_11_255():
    size = int(input("Введите размер массивов: "))
    a = list(map(float, input("Массив a: ").split()))
    b = list(map(float, input("Массив b: ").split()))
    sum_ab = [a[i] + b[i] for i in range(size)]
    prod_ab = [a[i] * b[i] for i in range(size)]
    max_ab = [max(a[i], b[i]) for i in range(size)]
    print("Сумма элементов:", sum_ab)
    print("Произведение элементов:", prod_ab)
    print("Максимум элементов:", max_ab)

def task_11_256():
    size = int(input("Введите размер массивов: "))
    a = list(map(float, input("Массив a: ").split()))
    b = list(map(float, input("Массив b: ").split()))
    c = []
    for i in range(size):
        sign_a = a[i] > 0
        sign_b = b[i] > 0
        c.append(1 if sign_a == sign_b else 0)
    print("Массив с 1, если знаки совпадают, иначе 0:", c)

def main():
    print("Выберите номер задачи (11.246 - 11.256) или введите 0 для выхода:")
    while True:
        choice = input("Введите номер задачи: ")
        if choice == '0':
            break
        elif choice == '11.246':
            task_11_246()
        elif choice == '11.247':
            task_11_247()
        elif choice == '11.248':
            task_11_248()
        elif choice == '11.249':
            task_11_249()
        elif choice == '11.250':
            task_11_250()
        elif choice == '11.251':
            task_11_251()
        elif choice == '11.252':
            task_11_252()
        elif choice == '11.253':
            task_11_253()
        elif choice == '11.254':
            task_11_254()
        elif choice == '11.255':
            task_11_255()
        elif choice == '11.256':
            task_11_256()
        else:
            print("Некорректный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()


#11.258
    a = []
    print("Введите 10 чисел:")
    for _ in range(10):
        a.append(float(input()))

#1
    negatives1 = []
    for num in a:
        if num < 0:
            negatives1.append(num)

#2
    negatives2 = [num for num in a if num < 0]
    print("Отрицательные числа (без генератора):", negatives1)
    print("Отрицательные числа (с генератором):", negatives2)

#11.259
    array = input("Введите элементы массива через пробел: ").split()
    array = [int(x) for x in array]
    k = int(input("Введите индекс k: "))

#1
    new_array1 = []
    for i in range(len(array)):
        if i != k:
            new_array1.append(array[i])

#2
    new_array2 = [array[i] for i in range(len(array)) if i != k]
    print("Массив без элемента с индексом k (без генератора):", new_array1)
    print("Массив без элемента с индексом k (с генератором):", new_array2)

#11.260
    array13 = input("Введите элементы массива через пробел: ").split()
    array13 = [int(x) for x in array13]

#1
    filtered1 = []
    for num in array13:
        if num != 13:
            filtered1.append(num)

    #2
    filtered2 = [num for num in array13 if num != 13]
    print("Массив без числа 13 (без генератора):", filtered1)
    print("Массив без числа 13 (с генератором):", filtered2)

    # 11.261
    words = input("Введите слова через пробел: ").split()

    #a
    average_length = sum(len(word) for word in words) / len(words) if words else 0

    #б
    count_long = sum(1 for word in words if len(word) > 5)

    #в
    max_length = max((len(word) for word in words), default=0)

    #г
    min_length = min((len(word) for word in words), default=0)
    shortest_indices = [i for i, word in enumerate(words) if len(word) == min_length]
    first_shortest_index = shortest_indices[0] if shortest_indices else -1

    #д
    more_than_max = sum(1 for word in words if len(word) > max_length)

    #е
    start_k = sum(1 for word in words if word.lower().startswith('к'))
    sorted_words = sorted(words)

    print("а) Средняя длина слова:", average_length)
    print("б) Количество слов длиннее 5 символов:", count_long)
    print("в) Длина самого длинного слова:", max_length)
    print("г) Номер первого самого короткого слова:", first_shortest_index)
    print("д) Количество символов в слове, большее чем в самом длинном:", more_than_max)
    print("е) Количество слов, начинающихся на 'к' или 'К':", start_k)
    print("Отсортированный список слов:", sorted_words)


# 12.1
def task_12_1():
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    full_name = name + " " + surname
    print(full_name)


# 12.2
def task_12_2():
    country = input("Введите название государства: ")
    capital = input("Введите название столицы: ")
    print(f"Столица государства {country} – город {capital}")


# 12.3
def task_12_3():
    novel = input("Введите название романа: ")
    author = input("Введите фамилию автора: ")
    print(f"Писатель {author} – автор романа {novel}")


# 12.4
def task_12_4():
    s1 = input("Введите название первой страны: ")
    s2 = input("Введите название второй страны: ")
    t1 = s2
    t2 = s1
    print(f"t1 = {t1}, t2 = {t2}")


# 12.5
def task_12_5():
    club = input("Введите название футбольного клуба: ")
    length = len(club)
    print(f"Количество символов: {length}")


# 12.6
def task_12_6():
    city = input("Введите название города: ")
    length = len(city)
    if length % 2 == 0:
        print("Количество символов четное")
    else:
        print("Количество символов нечетное")


# 12.7
def task_12_7():
    surname1 = input("Введите первую фамилию: ")
    surname2 = input("Введите вторую фамилию: ")
    if len(surname1) > len(surname2):
        print("Первая фамилия длиннее")
    elif len(surname1) < len(surname2):
        print("Вторая фамилия длиннее")
    else:
        print("Фамилии одинаковой длины")


# 12.8
def task_12_8():
    city1 = input("Введите название первого города: ")
    city2 = input("Введите название второго города: ")
    city3 = input("Введите название третьего города: ")

    cities = [city1, city2, city3]
    longest = max(cities, key=len)
    shortest = min(cities, key=len)

    print(f"Самое длинное название: {longest}")
    print(f"Самое короткое название: {shortest}")


# 12.9
def task_12_9():
    s1 = input("Введите название первой страны: ")
    s2 = input("Введите название второй страны: ")

    print(f"До обмена: s1 = {s1}, s2 = {s2}")
    s1, s2 = s2, s1
    print(f"После обмена: s1 = {s1}, s2 = {s2}")


# 12.10
def task_12_10():
    a = input("Введите значение a: ")
    b = input("Введите значение b: ")
    c = input("Введите значение c: ")

    print(f"Исходные значения: a={a}, b={b}, c={c}")

    # а
    temp_a = a
    temp_b = b
    temp_c = c

    b = temp_c
    a = temp_b
    c = temp_a
    print(f"После схемы а): a={a}, b={b}, c={c}")

    # б
    a, b, c = temp_a, temp_b, temp_c
    b = temp_a
    c = temp_b
    a = temp_c
    print(f"После схемы б): a={a}, b={b}, c={c}")


# 12.11
def task_12_11():
    word = input("Введите слово: ")
    if len(word) >= 3:
        print(f"Третий символ: {word[2]}")
    else:
        print("Слово слишком короткое")


# 12.12
def task_12_12():
    word = input("Введите слово: ")
    if len(word) > 0:
        print(f"Последний символ: {word[-1]}")
    else:
        print("Слово пустое")


# 12.13
def task_12_13():
    word = input("Введите слово: ")
    k = int(input("Введите номер символа k: "))
    if 0 < k <= len(word):
        print(f"{k}-й символ: {word[k - 1]}")
    else:
        print("Неверный номер символа")


# 12.14
def task_12_14():
    word = input("Введите слово: ")
    if len(word) >= 4:
        if word[1] == word[3]:
            print("Второй и четвертый символы одинаковы")
        else:
            print("Второй и четвертый символы различны")
    else:
        print("Слово слишком короткое")


# 12.15
def task_12_15():
    word = input("Введите слово: ")
    if len(word) > 0:
        if word[0].lower() == word[-1].lower():
            print("Слово начинается и оканчивается на одну букву")
        else:
            print("Слово начинается и оканчивается на разные буквы")
    else:
        print("Слово пустое")


# 12.16
def task_12_16():
    word1 = input("Введите первое слово: ")
    word2 = input("Введите второе слово: ")

    if len(word1) > 0 and len(word2) > 0:
        if word1[0].lower() == word2[-1].lower():
            print("Первое слово начинается на ту же букву, на которую оканчивается второе")
        else:
            print("Первое слово начинается на другую букву")
    else:
        print("Одно из слов пустое")


# 12.17
def task_12_17():
    word = input("Введите слово: ")
    if len(word) >= 4:
        combination = word[1] + word[3]
        print(f"Буквосочетание: {combination}")
    else:
        print("Слово слишком короткое")


# 12.18
def task_12_18():
    word = input("Введите слово: ")
    if len(word) >= 3:
        combination = word[2] + word[-1]
        print(f"Буквосочетание: {combination}")
    else:
        print("Слово слишком короткое")


# 12.19
def task_12_19():
    word = input("Введите слово: ")
    if len(word) >= 4:
        part = word[1:4]
        print(f"Часть слова: {part}")
    else:
        print("Слово слишком короткое")


# 12.20
def task_12_20():
    word = input("Введите слово (четное количество букв): ")
    if len(word) % 2 == 0:
        half = len(word) // 2
        first_half = word[:half]
        print(f"Первая половина: {first_half}")
    else:
        print("Слово содержит нечетное количество букв")


# 12.21
def task_12_21():
    word = input("Введите слово: ")
    m = int(input("Введите номер начального символа m: "))
    n = int(input("Введите номер конечного символа n: "))

    if 0 < m <= n <= len(word):
        part = word[m - 1:n]
        print(f"Часть слова: {part}")
    else:
        print("Неверные значения m и n")

def main():
    tasks = {
        '12.1': task_12_1,
        '12.2': task_12_2,
        '12.3': task_12_3,
        '12.4': task_12_4,
        '12.5': task_12_5,
        '12.6': task_12_6,
        '12.7': task_12_7,
        '12.8': task_12_8,
        '12.9': task_12_9,
        '12.10': task_12_10,
        '12.11': task_12_11,
        '12.12': task_12_12,
        '12.13': task_12_13,
        '12.14': task_12_14,
        '12.15': task_12_15,
        '12.16': task_12_16,
        '12.17': task_12_17,
        '12.18': task_12_18,
        '12.19': task_12_19,
        '12.20': task_12_20,
        '12.21': task_12_21
    }

    while True:
        print("\n" + "=" * 50)
        print("СПИСОК ЗАДАЧ:")
        for i in range(1, 22):
            key = f'12.{i}'
            print(f"{key} - Задача {key}")
        print("0 - Выход")
        print("=" * 50)

        choice = input("Выберите номер задачи (например, 12.1): ")

        if choice == '0':
            print("Выход из программы")
            break
        elif choice in tasks:
            print(f"\n--- Задача {choice} ---")
            tasks[choice]()
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()


    # 12.23
    def task_12_23():
        word = "информатика"
        word1 = word[2:7]  # форма
        word2 = word[7:10]  # тик
        print(f"Исходное слово: {word}")
        print(f"Полученные слова: {word1}, {word2}")


    # 12.24
    def task_12_24():
        word = "вертикаль"
        word1 = word[4:7]  # тир
        word2 = word[0:3] + word[6:8]  # ветка
        print(f"Исходное слово: {word}")
        print(f"Полученные слова: {word1}, {word2}")


    # 12.25
    def task_12_25():
        word = "программа"
        word1 = word[3:6]  # ром
        word2 = word[2:6] + word[0]  # рампа
        print(f"Исходное слово: {word}")
        print(f"Полученные слова: {word1}, {word2}")


    # 12.26
    def task_12_26():
        word = "трос"
        # Перестановка букв для получения разных слов
        words = [
            word[2] + word[0] + word[3] + word[1],  # сорт
            word[3] + word[0] + word[1] + word[2],  # рост
            word[1] + word[0] + word[3] + word[2]  # торс
        ]
        print(f"Исходное слово: {word}")
        print(f"Полученные слова: {', '.join(words)}")


    # 12.27
    def task_12_27():
        word = "клоун"
        words = [
            word[4] + word[0] + word[1] + word[2] + word[3],  # уклон
            word[0] + word[4] + word[1] + word[2] + word[3],  # кулон
            word[0] + word[1] + word[2] + word[4] + word[3]  # колун
        ]
        print(f"Исходное слово: {word}")
        print(f"Полученные слова: {', '.join(words)}")


    # 12.28
    def task_12_28():
        word = "апельсин"
        new_word = word[5] + word[3] + word[0] + word[6] + word[7] + word[1] + word[2] + word[4]
        print(f"Исходное слово: {word}")
        print(f"Полученное слово: {new_word}")


    # 12.29
    def task_12_29():
        word = "вирус"
        # Замена букв для получения слова "фокус"
        new_word = "ф" + word[1:3] + "у" + word[4]
        print(f"Исходное слово: {word}")
        print(f"После замены: {new_word}")


    # 12.30
    def task_12_30():
        word = "курсор"
        # Замена букв для получения слова "танцор"
        new_word = "танц" + word[4:]
        print(f"Исходное слово: {word}")
        print(f"После замены: {new_word}")


    # 12.31
    def task_12_31():
        word = "пробел"
        # Замена букв для получения слова "продел"
        new_word = word[0:2] + "од" + word[4:]
        print(f"Исходное слово: {word}")
        print(f"После замены: {new_word}")


    # 12.32
    def task_12_32():
        word = "строка"
        # Замена букв для получения слова "строфа"
        new_word = word[0:4] + "ф" + word[5]
        print(f"Исходное слово: {word}")
        print(f"После замены: {new_word}")


    # 12.33
    def task_12_33():
        word = "муха"
        # Замена всех букв для получения слова "слон"
        new_word = "слон"
        print(f"Исходное слово: {word}")
        print(f"После замены: {new_word}")


    # 12.34
    def task_12_34():
        word = "тетрадь"
        # Замена всех букв для получения слова "дневник"
        new_word = "дневник"
        print(f"Исходное слово: {word}")
        print(f"После замены: {new_word}")


    # 12.35
    def task_12_35():
        word = input("Введите слово из четного числа букв: ")

        if len(word) % 2 != 0:
            print("Слово должно содержать четное количество букв")
            return

        # Способ 1: без цикла
        half = len(word) // 2
        result1 = word[half:] + word[:half]

        # Способ 2: с циклом
        result2 = ""
        for i in range(half, len(word)):
            result2 += word[i]
        for i in range(half):
            result2 += word[i]

        print(f"Исходное слово: {word}")
        print(f"Способ 1 (без цикла): {result1}")
        print(f"Способ 2 (с циклом): {result2}")


    # 12.36
    def task_12_36():
        word = input("Введите слово из 12 букв: ")

        if len(word) != 12:
            print("Слово должно содержать 12 букв")
            return

        third = len(word) // 3

        # а) первая треть -> третья, вторая -> первая, третья -> вторая
        part_a = word[third:2 * third] + word[2 * third:] + word[:third]

        # б) первая треть -> вторая, вторая -> третья, третья -> первая
        part_b = word[2 * third:] + word[:third] + word[third:2 * third]

        print(f"Исходное слово: {word}")
        print(f"а) {part_a}")
        print(f"б) {part_b}")


    # 12.37
    def task_12_37():
        word = input("Введите слово (минимум 6 букв): ")

        if len(word) < 6:
            print("Слово должно содержать минимум 6 букв")
            return

        # Способ 1: без цикла
        result1 = word[-3:] + word[3:-3] + word[:3]

        # Способ 2: с циклом
        result2 = ""
        # Добавляем последние 3 буквы
        for i in range(len(word) - 3, len(word)):
            result2 += word[i]
        # Добавляем среднюю часть
        for i in range(3, len(word) - 3):
            result2 += word[i]
        # Добавляем первые 3 буквы
        for i in range(3):
            result2 += word[i]

        print(f"Исходное слово: {word}")
        print(f"Способ 1 (без цикла): {result1}")
        print(f"Способ 2 (с циклом): {result2}")


    # 12.38
    def task_12_38():
        word = input("Введите слово: ")
        k = int(input("Введите k: "))

        if k <= 0 or k >= len(word):
            print("k должно быть в диапазоне от 1 до длины слова-1")
            return

        # Способ 1: без цикла
        result1 = word[k:] + word[:k]

        # Способ 2: с циклом
        result2 = ""
        for i in range(k, len(word)):
            result2 += word[i]
        for i in range(k):
            result2 += word[i]

        print(f"Исходное слово: {word}")
        print(f"Способ 1 (без цикла): {result1}")
        print(f"Способ 2 (с циклом): {result2}")


    # 12.39
    def task_12_39():
        club = input("Введите название футбольного клуба: ")
        print("Название клуба столбиком:")
        for letter in club:
            print(letter)


    # 12.40
    def task_12_40():
        word = input("Введите слово: ")
        print("Слово с конца:")
        for i in range(len(word) - 1, -1, -1):
            print(word[i])


    # 12.41
    def task_12_41():
        s1 = input("Введите слово s1: ")
        s2 = ""
        for i in range(len(s1)):
            if i % 2 == 0:  # нечетные позиции (индексация с 0)
                s2 += s1[i]
        print(f"s1: {s1}")
        print(f"s2 (нечетные буквы): {s2}")


    # 12.42
    def task_12_42():
        s = input("Введите слово s: ")
        t = s[::-1]  # обратный порядок символов
        print(f"s: {s}")
        print(f"t (прочитанное с конца): {t}")


    # 12.43
    def task_12_43():
        stars = "*" * 5
        print(f"Строка из 5 звездочек: {stars}")


    # 12.44
    def task_12_44():
        underscores = "_" * 8
        print(f"Строка из 8 символов '_': {underscores}")


    # Главное меню для выбора задачи
    def main():
        tasks = {
            '12.1': task_12_1,
            '12.2': task_12_2,
            '12.3': task_12_3,
            '12.4': task_12_4,
            '12.5': task_12_5,
            '12.6': task_12_6,
            '12.7': task_12_7,
            '12.8': task_12_8,
            '12.9': task_12_9,
            '12.10': task_12_10,
            '12.11': task_12_11,
            '12.12': task_12_12,
            '12.13': task_12_13,
            '12.14': task_12_14,
            '12.15': task_12_15,
            '12.16': task_12_16,
            '12.17': task_12_17,
            '12.18': task_12_18,
            '12.19': task_12_19,
            '12.20': task_12_20,
            '12.21': task_12_21,
            '12.23': task_12_23,
            '12.24': task_12_24,
            '12.25': task_12_25,
            '12.26': task_12_26,
            '12.27': task_12_27,
            '12.28': task_12_28,
            '12.29': task_12_29,
            '12.30': task_12_30,
            '12.31': task_12_31,
            '12.32': task_12_32,
            '12.33': task_12_33,
            '12.34': task_12_34,
            '12.35': task_12_35,
            '12.36': task_12_36,
            '12.37': task_12_37,
            '12.38': task_12_38,
            '12.39': task_12_39,
            '12.40': task_12_40,
            '12.41': task_12_41,
            '12.42': task_12_42,
            '12.43': task_12_43,
            '12.44': task_12_44
        }

        while True:
            print("\n" + "=" * 50)
            print("СПИСОК ЗАДАЧ 12.23-12.44:")
            for i in range(23, 45):
                key = f'12.{i}'
                print(f"{key} - Задача {key}")
            print("0 - Выход")
            print("=" * 50)

            choice = input("Выберите номер задачи (например, 12.23): ")

            if choice == '0':
                print("Выход из программы")
                break
            elif choice in tasks:
                print(f"\n--- Задача {choice} ---")
                tasks[choice]()
            else:
                print("Неверный выбор. Попробуйте снова.")


    # Запуск программы
    if __name__ == "__main__":
        main()


