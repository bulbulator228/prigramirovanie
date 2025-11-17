#10.18
import random
def multiplication_test_single():
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    correct_answer = a * b
    print(f"Чему равно произведение {a}×{b}?")
    user_answer = int(input("Ваш ответ: "))
    if user_answer == correct_answer:
        print("Правильно!")
    else:
        print(f"Неправильно! Правильный ответ: {correct_answer}")
multiplication_test_single()

#b
import random
def multiplication_test_20():
    correct_count = 0
    incorrect_count = 0
    for i in range(20):
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        correct_answer = a * b
        print(f"Вопрос {i + 1}: Чему равно произведение {a}×{b}?")
        user_answer = int(input("Ваш ответ: "))
        if user_answer == correct_answer:
            print("Правильно!")
            correct_count += 1
        else:
            print(f"Неправильно! Правильный ответ: {correct_answer}")
            incorrect_count += 1
        print()
    print(f"Результаты:")
    print(f"Правильных ответов: {correct_count}")
    print(f"Неправильных ответов: {incorrect_count}")
multiplication_test_20()

#v
import random
def multiplication_test_until_zero():
    while True:
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        correct_answer = a * b
        print(f"Чему равно произведение {a}×{b}?")
        user_answer = int(input("Ваш ответ (0 для выхода): "))
        if user_answer == 0:
            print("Выход из программы.")
            break
        elif user_answer == correct_answer:
            print("Правильно!")
        else:
            print(f"Неправильно! Правильный ответ: {correct_answer}")
        print()
multiplication_test_until_zero()

#10.19
import random
def single_suit_card():
    cards = ["6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
    card = random.choice(cards)
    print(f"Выбрана карта: {card}")
    return card
single_suit_card()

#10.20
import random
def full_deck_card():
    suits = ["пик", "треф", "бубен", "червей"]
    ranks = ["6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
    suit = random.choice(suits)
    rank = random.choice(ranks)
    if rank == "6":
        rank_name = "шестерка"
    elif rank == "7":
        rank_name = "семерка"
    elif rank == "8":
        rank_name = "восьмерка"
    elif rank == "9":
        rank_name = "девятка"
    elif rank == "10":
        rank_name = "десятка"
    else:
        rank_name = rank

    print(f"Выбрана {rank_name} {suit}")
    return rank, suit
full_deck_card()

#10.21
import random
def compare_two_cards():
    suits = ["пик", "треф", "бубен", "червей"]
    ranks = ["6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
    def get_card_name(rank):
        if rank == "6":
            return "шестерка"
        elif rank == "7":
            return "семерка"
        elif rank == "8":
            return "восьмерка"
        elif rank == "9":
            return "девятка"
        elif rank == "10":
            return "десятка"
        else:
            return rank
    suit1 = random.choice(suits)
    rank1 = random.choice(ranks)
    suit2 = random.choice(suits)
    rank2 = random.choice(ranks)
    print(f"Игрок 1: {get_card_name(rank1)} {suit1}")
    print(f"Игрок 2: {get_card_name(rank2)} {suit2}")
    suit1_index = suits.index(suit1)
    suit2_index = suits.index(suit2)
    if suit1_index > suit2_index:
        print("Победил Игрок 1! (по масти)")
        return 1
    elif suit1_index < suit2_index:
        print("Победил Игрок 2! (по масти)")
        return 2
    else:
        rank1_index = ranks.index(rank1)
        rank2_index = ranks.index(rank2)
        if rank1_index > rank2_index:
            print("Победил Игрок 1! (по достоинству)")
            return 1
        elif rank1_index < rank2_index:
            print("Победил Игрок 2! (по достоинству)")
            return 2
        else:
            print("Ничья! Карты одинаковые")
            return 0
print("\n=== Задача 10.21 ===")
compare_two_cards()

#10.22
import random
def multiple_card_games():
    suits = ["пик", "треф", "бубен", "червей"]
    ranks = ["6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
    def get_card_name(rank):
        names = {"6": "шестерка", "7": "семерка", "8": "восьмерка",
                 "9": "девятка", "10": "десятка"}
        return names.get(rank, rank)
    def compare_cards(rank1, suit1, rank2, suit2):
        suit1_index = suits.index(suit1)
        suit2_index = suits.index(suit2)

        if suit1_index > suit2_index:
            return 1
        elif suit1_index < suit2_index:
            return 2
        else:
            rank1_index = ranks.index(rank1)
            rank2_index = ranks.index(rank2)
            if rank1_index > rank2_index:
                return 1
            elif rank1_index < rank2_index:
                return 2
            else:
                return 0
    player1_wins = 0
    player2_wins = 0
    draws = 0
    print("Игра начинается! Для выхода введите 'стоп'")
    round_number = 1
    while True:
        print(f"\n--- Раунд {round_number} ---")
        suit1 = random.choice(suits)
        rank1 = random.choice(ranks)
        suit2 = random.choice(suits)
        rank2 = random.choice(ranks)
        print(f"Игрок 1: {get_card_name(rank1)} {suit1}")
        print(f"Игрок 2: {get_card_name(rank2)} {suit2}")
        result = compare_cards(rank1, suit1, rank2, suit2)
        if result == 1:
            print("Победил Игрок 1!")
            player1_wins += 1
        elif result == 2:
            print("Победил Игрок 2!")
            player2_wins += 1
        else:
            print("Ничья!")
            draws += 1
        print(f"\nСтатистика после {round_number} раундов:")
        print(f"Игрок 1: {player1_wins} побед")
        print(f"Игрок 2: {player2_wins} побед")
        print(f"Ничьих: {draws}")
        user_input = input("\nНажмите Enter для следующего раунда или 'стоп' для выхода: ")
        if user_input.lower() == 'стоп':
            break
        round_number += 1
    print("\nИгра завершена!")
    print(f"Итоговый счет: Игрок 1 - {player1_wins}, Игрок 2 - {player2_wins}, Ничьих - {draws}")
    if player1_wins > player2_wins:
        print("Победил Игрок 1!")
    elif player2_wins > player1_wins:
        print("Победил Игрок 2!")
    else:
        print("Ничья по итогам всех раундов!")
print("\n=== Задача 10.22 ===")
multiple_card_games()

#10.23
import random
def trump_card_game():
    suits = ["пик", "треф", "бубен", "червей"]
    ranks = ["6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
    trump_suit = random.choice(suits)
    print(f"Козырная масть: {trump_suit}")
    suit = random.choice(suits)
    rank = random.choice(ranks)
    if rank == "6":
        rank_name = "шестерка"
    elif rank == "7":
        rank_name = "семерка"
    elif rank == "8":
        rank_name = "восьмерка"
    elif rank == "9":
        rank_name = "девятка"
    elif rank == "10":
        rank_name = "десятка"
    else:
        rank_name = rank
    if suit == trump_suit:
        print(f"Выбрана {rank_name} {suit} (козырная!)")
    else:
        print(f"Выбрана {rank_name} {suit}")
    return rank, suit, trump_suit
trump_card_game()

#10.24
import random
def rook_not_threatening():
    while True:
        a, b, c, d = [random.randint(1, 8) for _ in range(4)]
        if not (a == c or b == d):
            print(f"Ладья на ({a},{b}) не угрожает полю ({c},{d})")
            print("Проверка: ладья бьет по вертикали и горизонтали")
            return a, b, c, d
rook_not_threatening()

#b
import random
def bishop_not_threatening():
    while True:
        a, b, c, d = [random.randint(1, 8) for _ in range(4)]
        if abs(a - c) != abs(b - d):
            print(f"Слон на ({a},{b}) не угрожает полю ({c},{d})")
            print("Проверка: слон бьет по диагоналям")
            return a, b, c, d
bishop_not_threatening()

#v
import random
def king_one_move():
    while True:
        a, b, c, d = [random.randint(1, 8) for _ in range(4)]
        if abs(a - c) <= 1 and abs(b - d) <= 1 and (a != c or b != d):
            print(f"Король на ({a},{b}) может попасть на поле ({c},{d}) за один ход")
            print("Проверка: король ходит на одну клетку в любом направлении")
            return a, b, c, d
king_one_move()

#g
import random
def queen_not_threatening():
    while True:
        a, b, c, d = [random.randint(1, 8) for _ in range(4)]
        if not (a == c or b == d or abs(a - c) == abs(b - d)):
            print(f"Ферзь на ({a},{b}) не угрожает полю ({c},{d})")
            print("Проверка: ферзь бьет по вертикали, горизонтали и диагоналям")
            return a, b, c, d
queen_not_threatening()

#10.25
import random
def chess_pieces():
#а
    print("\nа) Белая пешка - обычный ход:")
    while True:
        a, b, c, d = [random.randint(1, 8) for _ in range(4)]
        if a == c and d == b + 1:
            print(f"Белая пешка на ({a},{b}) может пойти на ({c},{d}) обычным ходом")
            print("Проверка: пешка движется вперед на одну клетку")
            break

#а
    print("\nа) Белая пешка - взятие:")
    while True:
        a, b, c, d = [random.randint(1, 8) for _ in range(4)]
        if abs(a - c) == 1 and d == b + 1:
            print(f"Белая пешка на ({a},{b}) может пойти на ({c},{d}) взятием")
            print("Проверка: пешка бьет по диагонали вперед")
            break

#б
    print("\nб) Черная пешка - обычный ход:")
    while True:
        a, b, c, d = [random.randint(1, 8) for _ in range(4)]
        if a == c and d == b - 1:
            print(f"Черная пешка на ({a},{b}) может пойти на ({c},{d}) обычным ходом")
            print("Проверка: пешка движется вперед на одну клетку (вниз)")
            break

#б
    print("\nб) Черная пешка - взятие:")
    while True:
        a, b, c, d = [random.randint(1, 8) for _ in range(4)]
        if abs(a - c) == 1 and d == b - 1:
            print(f"Черная пешка на ({a},{b}) может пойти на ({c},{d}) взятием")
            print("Проверка: пешка бьет по диагонали вперед (вниз)")
            break

#в
    print("\nв) Конь угрожает полю:")
    while True:
        a, b, c, d = [random.randint(1, 8) for _ in range(4)]
        # Конь ходит буквой "Г": разность 2 и 1 или 1 и 2
        if (abs(a - c) == 2 and abs(b - d) == 1) or (abs(a - c) == 1 and abs(b - d) == 2):
            print(f"Конь на ({a},{b}) угрожает полю ({c},{d})")
            print("Проверка: конь ходит буквой 'Г'")
            break
chess_pieces()

#10.26
import random
def chess_figures_interaction():
    print("\n=== Задача 10.26 ===")

    def can_rook_move(a, b, e, f):
        return a == e or b == f
    def can_bishop_move(a, b, e, f):
        return abs(a - e) == abs(b - f)
    def can_queen_move(a, b, e, f):
        return a == e or b == f or abs(a - e) == abs(b - f)
    def can_knight_move(a, b, e, f):
        return (abs(a - e) == 2 and abs(b - f) == 1) or (abs(a - e) == 1 and abs(b - f) == 2)
    def can_king_move(a, b, e, f):
        return abs(a - e) <= 1 and abs(b - f) <= 1 and (a != e or b != f)
    def is_under_attack(fig_type, x, y, target_x, target_y):
        if fig_type == 'ладья':
            return x == target_x or y == target_y
        elif fig_type == 'слон':
            return abs(x - target_x) == abs(y - target_y)
        elif fig_type == 'ферзь':
            return x == target_x or y == target_y or abs(x - target_x) == abs(y - target_y)
        elif fig_type == 'конь':
            return (abs(x - target_x) == 2 and abs(y - target_y) == 1) or (
                        abs(x - target_x) == 1 and abs(y - target_y) == 2)
        return False
    combinations = [
        ('ладья', 'ладья'), ('ладья', 'ферзь'), ('ладья', 'конь'), ('ладья', 'слон'),
        ('ферзь', 'ферзь'), ('ферзь', 'ладья'), ('ферзь', 'конь'), ('ферзь', 'слон'),
        ('конь', 'конь'), ('конь', 'ладья'), ('конь', 'ферзь'), ('конь', 'слон'),
        ('слон', 'слон'), ('слон', 'ферзь'), ('слон', 'конь'), ('слон', 'ладья'),
        ('король', 'слон'), ('король', 'ферзь'), ('король', 'конь'), ('король', 'ладья')
    ]
    for white_fig, black_fig in combinations[:3]:  # Покажем первые 3 комбинации
        print(f"\nКомбинация: {white_fig} (белая) vs {black_fig} (черная)")
        while True:
            a, b, c, d, e, f = [random.randint(1, 8) for _ in range(6)]
            white_can_move = False
            if white_fig == 'ладья':
                white_can_move = can_rook_move(a, b, e, f)
            elif white_fig == 'слон':
                white_can_move = can_bishop_move(a, b, e, f)
            elif white_fig == 'ферзь':
                white_can_move = can_queen_move(a, b, e, f)
            elif white_fig == 'конь':
                white_can_move = can_knight_move(a, b, e, f)
            elif white_fig == 'король':
                white_can_move = can_king_move(a, b, e, f)
            black_threatens = is_under_attack(black_fig, c, d, e, f)
            if white_can_move and not black_threatens:
                print(f"Белая {white_fig} на ({a},{b}) может пойти на ({e},{f})")
                print(f"Черная {black_fig} на ({c},{d}) не угрожает полю ({e},{f})")
                break
chess_figures_interaction()

#10.27
import random
import math
def monte_carlo_area():

#а
    print("а) Площадь под половиной синусоиды (0 до π):")
    def area_under_sine():
        n = 100000
        count_under = 0
        for _ in range(n):
            x = random.uniform(0, math.pi)
            y = random.uniform(0, 1)  # Максимум синуса = 1
            if y <= math.sin(x):
                count_under += 1
        area = (count_under / n) * math.pi  # Площадь прямоугольника π × 1
        exact_area = 2  # ∫sin(x)dx от 0 до π = 2
        error = abs(area - exact_area)
        print(f"Вычисленная площадь: {area:.6f}")
        print(f"Точная площадь: {exact_area:.6f}")
        print(f"Погрешность: {error:.6f}")
        return area
    area_under_sine()

#б
    print("\nб) Площадь под параболой y = x² от 0 до 3:")
    def area_under_parabola():
        n = 100000
        count_under = 0
        for _ in range(n):
            x = random.uniform(0, 3)
            y = random.uniform(0, 9)  # Максимум 3² = 9
            if y <= x ** 2:
                count_under += 1
        area = (count_under / n) * 27  # Площадь прямоугольника 3 × 9 = 27
        exact_area = 9
        error = abs(area - exact_area)
        print(f"Вычисленная площадь: {area:.6f}")
        print(f"Точная площадь: {exact_area:.6f}")
        print(f"Погрешность: {error:.6f}")
        return area
    area_under_parabola()
monte_carlo_area()

#10.28
import random
import math
def monte_carlo_pi():
    print("Вычисление числа π методом Монте-Карло")
    def calculate_pi_with_precision(precision=0.0001):
        n = 0
        points_in_circle = 0
        points_total = 0
        current_pi = 0
        prev_pi = 0
        print("Вычисление π с точностью 0.0001:")
        print("Итерация | Точек | Вычисленное π | Погрешность")
        print("-" * 50)
        iteration = 0
        while True:
            iteration += 1
            batch_size = 10000
            for _ in range(batch_size):
                x = random.uniform(-1, 1)
                y = random.uniform(-1, 1)
                if x ** 2 + y ** 2 <= 1:
                    points_in_circle += 1
                points_total += 1
            prev_pi = current_pi
            current_pi = 4 * points_in_circle / points_total
            error = abs(current_pi - math.pi)
            if iteration % 10 == 0:  # Выводим каждые 10 итераций
                print(f"{iteration:8d} | {points_total:6d} | {current_pi:.6f} | {error:.6f}")
            if error < precision:
                break
        print("-" * 50)
        print(f"Финальный результат: π ≈ {current_pi:.6f}")
        print(f"Точное значение:     π = {math.pi:.6f}")
        print(f"Погрешность: {error:.6f}")
        print(f"Всего точек: {points_total}")
        return current_pi
    def calculate_pi_circle_area():
        print("\nАльтернативный метод (через площадь круга):")
        n = 1000000
        count_inside = 0
        for _ in range(n):
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            if x ** 2 + y ** 2 <= 1:
                count_inside += 1
        calculated_pi = 4 * count_inside / n
        error = abs(calculated_pi - math.pi)
        print(f"Вычисленное π: {calculated_pi:.6f}")
        print(f"Точное значение: {math.pi:.6f}")
        print(f"Погрешность: {error:.6f}")
        print(f"Точек в круге: {count_inside}/{n}")
        return calculated_pi
    pi1 = calculate_pi_with_precision()
    pi2 = calculate_pi_circle_area()
monte_carlo_pi()

#11.1
def task_11_1():
    print("=== Задача 11.1 ===")
    arr = [37, 0, 50, 46, 34, 46, 0, 13]
    print("Массив:", arr)
    return arr
task_11_1()

#11.2
def task_11_2():
    arr = []
    for i in range(10):
        value = int(input(f"Введите элемент {i+1}: "))
        arr.append(value)
    print("Полученный массив:", arr)
    return arr

#11.3
import random
def task_11_3():

#а
    arr_a = [random.random() for _ in range(15)]
    print("а) От 0 до 1:", [f"{x:.3f}" for x in arr_a])

#б
    arr_b = [random.uniform(22, 23) for _ in range(15)]
    print("б) От 22 до 23:", [f"{x:.3f}" for x in arr_b])

#в
    arr_c = [random.uniform(0, 10) for _ in range(15)]
    print("в) От 0 до 10:", [f"{x:.3f}" for x in arr_c])

#г
    arr_d = [random.uniform(-50, 50) for _ in range(15)]
    print("г) От -50 до 50:", [f"{x:.3f}" for x in arr_d])

#д
    arr_e = [random.randint(0, 10) for _ in range(15)]
    print("д) Целые от 0 до 10:", arr_e)
    return arr_a, arr_b, arr_c, arr_d, arr_e
task_11_3()

#11.4
def task_11_4():
    arr = ['#' for _ in range(20)]
    print("Массив:", arr)
    print("Строка:", ''.join(arr))
    return arr
task_11_4()

#11.5
def task_11_5():
    arr = [random.randint(163, 190) for _ in range(12)]
    print("Рост 12 человек:", arr)
    return arr
task_11_5()

#11.6
def task_11_6():
    arr = [random.randint(50, 100) for _ in range(20)]
    print("Вес 20 человек:", arr)
    return arr
task_11_6()

#11.7
def task_11_7():
    n = int(input("Введите размер массива: "))
    a = int(input("Введите начало интервала: "))
    b = int(input("Введите конец интервала: "))
    arr = [random.randint(a, b) for _ in range(n)]
    print(f"Массив из {n} элементов от {a} до {b}:", arr)
    return arr

#11.8
def task_11_8():
    arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print("Массив:", arr)
    index = int(input("Введите индекс элемента: "))
    if 0 <= index < len(arr):
        print(f"Элемент с индексом {index}: {arr[index]}")
    else:
        print("Неверный индекс!")
    return arr

#11.9
def task_11_9():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Исходный массив:", arr)
    print("В обратном порядке:", arr[::-1])
    return arr
task_11_9()

#11.10
def task_11_10():
    arr = list(range(1, 13))
    print("Массив от 1 до 12:", arr)
    return arr
task_11_10()

#11.11
def task_11_11():
    arr = list(range(1, 26))
    print("Первые 25 натуральных чисел:", arr)
    arr.append(100)
    arr.append(200)
    print("После добавления 100 и 200:", arr)
    return arr
task_11_11()

#11.12
def task_11_12():
    arr = list(range(20, 0, -1))
    print("Массив от 20 до 1:", arr)
    return arr
task_11_12()

#11.13
def task_11_13():
    n = int(input("Введите n: "))
    arr = [2**i for i in range(1, n+1)]
    print(f"Степени числа 2 от 2^1 до 2^{n}:", arr)
    return arr

#11.14
def task_11_14():
    n = int(input("Введите натуральное число (n ≤ 999999): "))
    arr = [0] * 6
    temp = n
    for i in range(6):
        if temp > 0:
            arr[i] = temp % 10
            temp //= 10
    print(f"Число: {n}")
    print("Цифры в обратном порядке:", arr)
    digits = [arr[i] for i in range(6) if i < len(str(n))]
    print("Цифры числа:", digits)
    return arr

#11.15
def task_11_15():

#а
    arr_a = list(range(15, 7, -1))
    print("а) Убывающая последовательность:", arr_a)

#б
    arr_b = list(range(5, 13))
    print("б) Возрастающая последовательность:", arr_b)
    return arr_a, arr_b
task_11_15()

#11.16
def task_11_16():

#а
    a = 2  # первый член
    p = 3  # разность
    arr_a = [a + i * p for i in range(10)]
    print(f"а) Арифметическая прогрессия (a={a}, p={p}):", arr_a)

#б
    a = 2  # первый член
    z = 3  # знаменатель
    arr_b = [a * (z ** i) for i in range(20)]
    print(f"б) Геометрическая прогрессия (a={a}, z={z}):", arr_b)
    return arr_a, arr_b
task_11_16()

#11.17
def task_11_17():
    arr = [0, 1]
    for i in range(2, 10):
        arr.append(arr[i - 1] + arr[i - 2])
    print("Первые 10 чисел Фибоначчи:", arr)
    return arr
task_11_17()

#11.18
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def task_11_18():

#а
    arr_a = []
    num = 300
    while len(arr_a) < 20:
        if num % 13 == 0 or num % 17 == 0:
            arr_a.append(num)
        num += 1
    print("а) 20 чисел от 300, делящихся на 13 или 17:", arr_a)

#б
    arr_b = []
    num = 2
    while len(arr_b) < 30:
        if is_prime(num):
            arr_b.append(num)
        num += 1
    print("б) Первые 30 простых чисел:", arr_b)
    return arr_a, arr_b
task_11_18()

#11.19
def task_11_19():
    arr = []
    num = 100
    while len(arr) < 10:
        if is_prime(num):
            arr.append(num)
        num += 1
    print("Первые 10 простых чисел, начиная с 100:", arr)
    return arr
task_11_19()

#11.20
import random
def multiplication_test_simple():
    print("=== ПРОВЕРКА ТАБЛИЦЫ УМНОЖЕНИЯ ===")
    user_answers = []
    for i in range(20):
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        print(f"\nВопрос {i + 1}:")
        print(f"Чему равно произведение {a} на {b}?")
        answer = int(input("Ваш ответ: "))
        user_answers.append(answer)
    print("\n" + "=" * 40)
    print("Массив ваших ответов:")
    print(user_answers)
    return user_answers
multiplication_test_simple()