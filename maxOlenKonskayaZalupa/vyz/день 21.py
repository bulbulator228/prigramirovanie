#11.21
import random
import math
def task_11_21():
    unique_numbers = random.sample(range(1, 101), 20)
    print("Массив с неповторяющимися числами:", unique_numbers)
    print("Длина массива:", len(unique_numbers))
    print("Уникальных чисел:", len(set(unique_numbers)))
    return unique_numbers
task_11_21()


def task_11_22_24():
    arr = [random.randint(-50, 150) for _ in range(15)]
    print("Исходный массив:", arr)

    # 11.22
    print("\n11.22 а) Все неотрицательные элементы:")
    non_negative = [x for x in arr if x >= 0]
    print(non_negative)

    print("11.22 б) Все элементы, не превышающие 100:")
    less_than_100 = [x for x in arr if x <= 100]
    print(less_than_100)

    # 11.23
    print("\n11.23 а) Все четные элементы:")
    even_numbers = [x for x in arr if x % 2 == 0]
    print(even_numbers)

    print("11.23 б) Все элементы, оканчивающиеся нулем:")
    ends_with_zero = [x for x in arr if abs(x) % 10 == 0]
    print(ends_with_zero)

    # 11.24
    natural_arr = [random.randint(1, 999) for _ in range(20)]
    print(f"\n11.24 Массив натуральных чисел: {natural_arr}")
    print("11.24 а) Двузначные числа:")
    two_digit = [x for x in natural_arr if 10 <= x <= 99]
    print(two_digit)

    print("11.24 б) Трехзначные числа:")
    three_digit = [x for x in natural_arr if 100 <= x <= 999]
    print(three_digit)
    return arr, natural_arr
task_11_22_24()


def task_11_25_27():
    arr = [random.randint(1, 100) for _ in range(12)]
    print("Исходный массив:", arr)

# 11.25
    print("\n11.25 а) Второй, четвертый и т.д. элементы:")
    even_positions = [arr[i] for i in range(1, len(arr), 2)]
    print(even_positions)
    print("11.25 б) Третий, шестой и т.д. элементы:")
    every_third = [arr[i] for i in range(2, len(arr), 3)]
    print(every_third)

# 11.26
    mixed_arr = [random.randint(-20, 20) for _ in range(10)]
    print(f"\n11.26 Массив со знаками: {mixed_arr}")
    non_negative = [x for x in mixed_arr if x >= 0]
    negative = [x for x in mixed_arr if x < 0]
    print("Сначала неотрицательные, затем отрицательные:")
    print(non_negative + negative)

# 11.27
    int_arr = [random.randint(1, 50) for _ in range(10)]
    print(f"\n11.27 Массив целых чисел: {int_arr}")
    even = [x for x in int_arr if x % 2 == 0]
    odd = [x for x in int_arr if x % 2 != 0]
    print("Сначала четные, затем нечетные:")
    print(even + odd)
    return arr, mixed_arr, int_arr
task_11_25_27()


def task_11_28_31():

# 11.28
    arr = [random.randint(1, 200) for _ in range(15)]
    print("11.28 Массив:", arr)
    indices_ending_zero = [i + 1 for i, x in enumerate(arr) if x % 10 == 0]
    print("Номера элементов, оканчивающихся на 0:", indices_ending_zero)

# 11.29
    january_precip = [random.randint(0, 10) for _ in range(31)]
    print(f"\n11.29 Осадки за январь: {january_precip}")
    dry_days = [i + 1 for i, x in enumerate(january_precip) if x == 0]
    print("Дни без осадков:", dry_days)

# 11.30
    team_wins = [random.randint(0, 10) for _ in range(20)]
    print(f"\n11.30 Победы 20 команд: {team_wins}")
    weak_teams = [i + 1 for i, x in enumerate(team_wins) if x < 3]
    print("Номера команд с менее чем 3 победами:", weak_teams)

# 11.31
    arr = [random.randint(1, 50) for _ in range(10)]
    print(f"\n11.31 Массив: {arr}")
    even_pos = [arr[i] for i in range(0, len(arr), 2)]  # четные позиции (0,2,4...)
    odd_pos = [arr[i] for i in range(1, len(arr), 2)]  # нечетные позиции (1,3,5...)
    print("Элементы на четных позициях:", even_pos)
    print("Элементы на нечетных позициях:", odd_pos)
    return arr, january_precip, team_wins
task_11_28_31()


def task_11_32_33():

# 11.32
    arr_32 = [round(random.uniform(-10, 10), 2) for _ in range(8)]
    print(f"11.32 Исходный массив: {arr_32}")

#а
    arr_32a = [abs(x) if x < 0 else x for x in arr_32]
    print("а) После замены отрицательных на модули:", [f"{x:.2f}" for x in arr_32a])

#б
    arr_32b = arr_32.copy()
    for i in range(len(arr_32b)):
        if i % 2 == 0:  # нечетные позиции (0,2,4...)
            arr_32b[i] = math.sqrt(abs(arr_32b[i]))
    print("б) После замены нечетных номеров на корень:", [f"{x:.2f}" for x in arr_32b])

# 11.33
    arr_33 = [round(random.uniform(0, 20), 2) for _ in range(8)]
    print(f"\n11.33 Исходный массив: {[f'{x:.2f}' for x in arr_33]}")

#а
    arr_33a = [math.sqrt(x) if x > 10 else x for x in arr_33]
    print("а) После замены >10 на корень:", [f"{x:.2f}" for x in arr_33a])

#б
    arr_33b = [abs(arr_33[i]) if i % 2 == 1 else arr_33[i] for i in range(len(arr_33))]
    print("б) После замены четных номеров на модуль:", [f"{x:.2f}" for x in arr_33b])
    return arr_32, arr_33
task_11_32_33()


def task_11_34_37():

    arr = [round(random.uniform(-10, 10), 2) for _ in range(10)]
    print(f"Исходный массив: {[f'{x:.2f}' for x in arr]}")

#11.34
    k1, k2 = 2, 5  # индексы элементов
    arr_34a = []
    for x in arr:
        if x > 0:
            arr_34a.append(x - arr[k1])
        else:
            arr_34a.append(x - arr[k2])
    print(f"\n11.34 а) После вычитания k1={k1}, k2={k2}: {[f'{x:.2f}' for x in arr_34a]}")
    arr_34b = [x + 1 if i % 2 == 0 else x - 1 for i, x in enumerate(arr)]
    print(f"11.34 б) Нечетные +1, четные -1: {[f'{x:.2f}' for x in arr_34b]}")

# 11.35
    m1, m2 = 1, 3
    arr_35a = []
    for x in arr:
        if x < 0:
            arr_35a.append(x + arr[m1])
        else:
            arr_35a.append(x + arr[m2])
    print(f"\n11.35 а) После прибавления m1={m1}, m2={m2}: {[f'{x:.2f}' for x in arr_35a]}")
    arr_35b = [x * 2 if i % 2 == 1 else x - 1 for i, x in enumerate(arr)]
    print(f"11.35 б) Четные ×2, нечетные -1: {[f'{x:.2f}' for x in arr_35b]}")

# 11.36
    k1, n = 2, 5
    arr_36a = []
    for x in arr:
        if x > 0:
            arr_36a.append(x - arr[k1])
        elif x < 0:
            arr_36a.append(x - n)
        else:
            arr_36a.append(x)
    print(f"\n11.36 а) Положительные -k1, отрицательные -n: {[f'{x:.2f}' for x in arr_36a]}")
    a, b, n = 2, 3, 1
    arr_36b = []
    for x in arr:
        if x > 0:
            arr_36b.append(x - a)
        elif x < 0:
            arr_36b.append(x + b)
        else:
            arr_36b.append(x + n)
    print(f"11.36 б) Комплексная модификация: {[f'{x:.2f}' for x in arr_36b]}")

# 11.37
    a1, b = 1, 2
    arr_37a = []
    for x in arr:
        if x < 0:
            arr_37a.append(x + arr[a1])
        elif x == 0:
            arr_37a.append(x - b)
        else:
            arr_37a.append(x)
    print(f"\n11.37 а) Отрицательные +a1, нулевые -b: {[f'{x:.2f}' for x in arr_37a]}")
    a, b, c = 1, 2, 3
    arr_37b = []
    for x in arr:
        if x > 0:
            arr_37b.append(x - a)
        elif x < 0:
            arr_37b.append(x - b)
        else:
            arr_37b.append(x + c)
    print(f"11.37 б) Комплексная модификация 2: {[f'{x:.2f}' for x in arr_37b]}")
    return arr
task_11_34_37()


def task_11_38_39():
    arr = [random.randint(1, 50) for _ in range(12)]
    print(f"Исходный массив: {arr}")

#11.38
    arr_38a = [x // 2 if x % 10 == 4 else x for x in arr]
    print(f"\n11.38 а) Элементы, оканчивающиеся на 4, уменьшены вдвое: {arr_38a}")
    arr_38b = [x ** 2 if x % 2 == 0 else x * 2 for x in arr]
    print(f"11.38 б) Четные в квадрате, нечетные удвоены: {arr_38b}")
    a, b = 5, 3
    arr_38c = arr.copy()
    for i in range(len(arr_38c)):
        if arr_38c[i] % 2 == 0:
            arr_38c[i] += a
        if i % 2 == 1:
            arr_38c[i] -= b
    print(f"11.38 в) Четные элементы +{a}, четные номера -{b}: {arr_38c}")

#11.39
    arr_39a = [0 if x % 10 == 0 else x for x in arr]
    print(f"\n11.39 а) Элементы, кратные 10, заменены на 0: {arr_39a}")
    arr_39b = [x * 2 if x % 2 != 0 else x // 2 for x in arr]
    print(f"11.39 б) Нечетные удвоены, четные уменьшены вдвое: {arr_39b}")
    m, n = 2, 3
    arr_39c = arr.copy()
    for i in range(len(arr_39c)):
        if arr_39c[i] % 2 != 0:
            arr_39c[i] -= m
        if i % 2 == 0:
            arr_39c[i] += n
    print(f"11.39 в) Нечетные элементы -{m}, нечетные номера +{n}: {arr_39c}")
    return arr
task_11_38_39()


def task_11_40_42():
    arr = [random.randint(1, 100) for _ in range(10)]
    print(f"Массив: {arr}")

#11.40
    element_index = random.randint(0, len(arr) - 1)
    sqrt_value = math.sqrt(arr[element_index])
    print(f"\n11.40 а) Квадратный корень из элемента {element_index + 1}: {sqrt_value:.2f}")
    idx1, idx2 = random.sample(range(len(arr)), 2)
    avg_value = (arr[idx1] + arr[idx2]) / 2
    print(f"11.40 б) Среднее арифметическое элементов {idx1 + 1} и {idx2 + 1}: {avg_value:.2f}")

#11.41
    s, k = 2, 5  # индексы (с 0)
    print(f"\n11.41 а) Элемент {s + 1} положительный: {arr[s] > 0}")
    print(f"11.41 б) Элемент {k + 1} четный: {arr[k] % 2 == 0}")
    if arr[k] > arr[s]:
        result = f"Элемент {k + 1} больше элемента {s + 1}"
    elif arr[k] < arr[s]:
        result = f"Элемент {s + 1} больше элемента {k + 1}"
    else:
        result = "Элементы равны"
    print(f"11.41 в) {result}")

#11.42
    total_sum = sum(arr)
    product = 1
    for x in arr:
        product *= x
    sum_of_squares = sum(x ** 2 for x in arr)
    sum_first_six = sum(arr[:6])
    k1, k2 = 2, 7
    sum_range_k = sum(arr[k1:k2 + 1])
    average_all = total_sum / len(arr)
    s1, s2 = 1, 8
    sum_range_s = sum(arr[s1:s2 + 1])
    average_range = sum_range_s / (s2 - s1 + 1)
    print(f"\n11.42 а) Сумма всех элементов: {total_sum}")
    print(f"11.42 б) Произведение всех элементов: {product}")
    print(f"11.42 в) Сумма квадратов: {sum_of_squares}")
    print(f"11.42 г) Сумма первых 6 элементов: {sum_first_six}")
    print(f"11.42 д) Сумма элементов с {k1 + 1} по {k2 + 1}: {sum_range_k}")
    print(f"11.42 е) Среднее арифметическое всех: {average_all:.2f}")
    print(f"11.42 ж) Среднее с {s1 + 1} по {s2 + 1}: {average_range:.2f}")
    return arr
task_11_40_42()

#11.43
def task_11_43_45():

#11.43
    arr = [random.randint(1, 20) for _ in range(10)]
    print(f"11.43 Массив: {arr}")
    alternating_sum = 0
    for i in range(len(arr)):
        alternating_sum += arr[i] * ((-1) ** i)
    print(f"Знакопеременная сумма: {alternating_sum}")

#11.44
    january_precip = [random.randint(0, 15) for _ in range(31)]
    total_january = sum(january_precip)
    print(f"\n11.44 Осадки за январь: {january_precip}")
    print(f"Общее количество осадков: {total_january}")

#11.45
    item_prices = [round(random.uniform(50, 500), 2) for _ in range(12)]
    total_cost = sum(item_prices)
    print(f"\n11.45 Стоимость 12 предметов: {[f'{p:.2f}' for p in item_prices]}")
    print(f"Общая стоимость: {total_cost:.2f}")
    return arr, january_precip, item_prices
task_11_43_45()

def task_11_46_50():

#11.46
    resistances_series = [round(random.uniform(1, 100), 2) for _ in range(20)]
    total_series = sum(resistances_series)
    print(f"11.46 Сопротивления (последовательно): {[f'{r:.2f}' for r in resistances_series]}")
    print(f"Общее сопротивление: {total_series:.2f} Ом")

#11.47
    resistances_parallel = [round(random.uniform(1, 100), 2) for _ in range(20)]
    total_parallel = 1 / sum(1 / r for r in resistances_parallel)
    print(f"\n11.47 Сопротивления (параллельно): {[f'{r:.2f}' for r in resistances_parallel]}")
    print(f"Общее сопротивление: {total_parallel:.2f} Ом")

#11.48
    june_precip = [random.randint(0, 20) for _ in range(30)]
    decade1 = sum(june_precip[:10])
    decade2 = sum(june_precip[10:20])
    decade3 = sum(june_precip[20:30])
    print(f"\n11.48 Осадки за июнь: {june_precip}")
    print(f"1-я декада: {decade1} мм, 2-я декада: {decade2} мм, 3-я декада: {decade3} мм")

#11.49
    feb_precip = [random.randint(0, 10) for _ in range(28)]
    avg_feb = sum(feb_precip) / len(feb_precip)
    print(f"\n11.49 Осадки за февраль: {feb_precip}")
    print(f"Среднедневное количество осадков: {avg_feb:.2f} мм")

#11.50
    sept_precip = [random.randint(0, 25) for _ in range(30)]
    avg_decade1 = sum(sept_precip[:10]) / 10
    avg_decade2 = sum(sept_precip[10:20]) / 10
    avg_decade3 = sum(sept_precip[20:30]) / 10
    print(f"\n11.50 Осадки за сентябрь: {sept_precip}")
    print(f"Среднее за 1-ю декаду: {avg_decade1:.2f} мм")
    print(f"Среднее за 2-ю декаду: {avg_decade2:.2f} мм")
    print(f"Среднее за 3-ю декаду: {avg_decade3:.2f} мм")
    return (resistances_series, resistances_parallel,
            june_precip, feb_precip, sept_precip)
task_11_46_50()