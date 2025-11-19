import random
import math


class ArrayTasks1151_1180:
    @staticmethod
    def task_11_51():
        arr = [random.randint(-10, 20) for _ in range(10)]
        total_sum = sum(arr)
        is_non_negative = total_sum >= 0
        print(f"Массив: {arr}")
        print(f"Сумма: {total_sum}, Неотрицательная: {is_non_negative}")
        return arr

    @staticmethod
    def task_11_52():
        int_arr = [random.randint(1, 50) for _ in range(15)]
        sum_arr = sum(int_arr)
        sum_squares = sum(x ** 2 for x in int_arr)
        print(f"Массив: {int_arr}")
        print(f"а) Сумма четная: {sum_arr % 2 == 0}")
        print(f"б) Сумма квадратов пятизначная: {10000 <= sum_squares <= 99999}")
        return int_arr

    @staticmethod
    def task_11_53():
        class_sizes = [random.randint(20, 35) for _ in range(42)]
        total_students = sum(class_sizes)
        is_four_digit = 1000 <= total_students <= 9999
        print(f"Численность 42 классов: {class_sizes}")
        print(f"Общее число учеников: {total_students}, Четырехзначное: {is_four_digit}")
        return class_sizes

    @staticmethod
    def task_11_54():
        books_per_section = [random.randint(100, 500) for _ in range(35)]
        total_books = sum(books_per_section)
        is_six_digit = 100000 <= total_books <= 999999
        print(f"Книги в 35 разделах: {books_per_section}")
        print(f"Общее число книг: {total_books}, Шестизначное: {is_six_digit}")
        return books_per_section

    @staticmethod
    def task_11_55():
        item_weights = [random.randint(10, 100) for _ in range(30)]
        truck_capacity = 1500
        total_weight = sum(item_weights)
        within_capacity = total_weight <= truck_capacity
        print(f"Веса 30 предметов: {item_weights}")
        print(f"Общая масса: {total_weight}, Грузоподъемность: {truck_capacity}")
        print(f"Не превышает: {within_capacity}")
        return item_weights

    @staticmethod
    def task_11_56():
        scores = [random.randint(700, 1000) for _ in range(10)]
        qualification_score = 8000
        total_score = sum(scores)
        qualified = total_score > qualification_score
        print(f"Баллы по 10 видам: {scores}")
        print(f"Общая сумма: {total_score}, Квалификация: {qualification_score}")
        print(f"Вышел в следующий этап: {qualified}")
        return scores

    @staticmethod
    def task_11_57():
        june_precip = [random.randint(0, 25) for _ in range(30)]
        first_half = sum(june_precip[:15])
        second_half = sum(june_precip[15:])
        decade1 = sum(june_precip[:10])
        decade2 = sum(june_precip[10:20])
        decade3 = sum(june_precip[20:30])
        max_decade = max(decade1, decade2, decade3)
        print(f"Осадки за июнь: {june_precip}")
        print(f"Первая половина: {first_half}, Вторая половина: {second_half}")
        print(f"Больше осадков в {'первой' if first_half > second_half else 'второй'} половине")
        print(f"По декадам: 1-я - {decade1}, 2-я - {decade2}, 3-я - {decade3}")
        print(f"Больше всего осадков в {['1-й', '2-й', '3-й'][[decade1, decade2, decade3].index(max_decade)]} декаде")
        return june_precip

    @staticmethod
    def task_11_58():
        scores_skating = [round(random.uniform(4.0, 6.0), 1) for _ in range(18)]
        compulsory = sum(scores_skating[:6])  # обязательная программа
        free = sum(scores_skating[6:])  # произвольная программа
        print(f"Оценки фигуриста: {scores_skating}")
        print(f"Обязательная программа: {compulsory:.1f}")
        print(f"Произвольная программа: {free:.1f}")
        print(f"Лучший результат в {'обязательной' if compulsory > free else 'произвольной'} программе")
        return scores_skating

    @staticmethod
    def task_11_59():
        arr = [random.randint(1, 100) for _ in range(15)]
        sum_under_20 = sum(x for x in arr if x <= 20)
        a = 50
        sum_above_a = sum(x for x in arr if x > a)
        print(f"Массив: {arr}")
        print(f"а) Сумма элементов ≤ 20: {sum_under_20}")
        print(f"б) Сумма элементов > {a}: {sum_above_a}")
        return arr

    @staticmethod
    def task_11_60():
        arr = [random.randint(1, 100) for _ in range(15)]
        sum_odd = sum(x for x in arr if x % 2 != 0)
        multiple_num = 7
        sum_multiples = sum(x for x in arr if x % multiple_num == 0)
        a, b = 3, 5
        sum_multiples_ab = sum(x for x in arr if x % a == 0 or x % b == 0)
        print(f"Массив: {arr}")
        print(f"а) Сумма нечетных: {sum_odd}")
        print(f"б) Сумма кратных {multiple_num}: {sum_multiples}")
        print(f"в) Сумма кратных {a} или {b}: {sum_multiples_ab}")
        return arr

    @staticmethod
    def task_11_61():
        arr = [random.randint(1, 100) for _ in range(15)]
        sum_even_positions = sum(arr[i] for i in range(1, len(arr), 2))
        print(f"Массив: {arr}")
        print(f"Сумма 2,4,6... элементов: {sum_even_positions}")
        return arr

    @staticmethod
    def task_11_62():
        feb_precip = [random.randint(0, 15) for _ in range(28)]
        sum_even_days = sum(feb_precip[i] for i in range(1, 28, 2))  # четные дни (2,4,6...)
        print(f"Осадки февраля: {feb_precip}")
        print(f"Сумма осадков по четным числам: {sum_even_days}")
        return feb_precip

    @staticmethod
    def task_11_63():
        monthly_precip = [random.randint(10, 100) for _ in range(12)]
        target_months = [2, 5, 8, 11]  # март, июнь, сентябрь, декабрь (индексы 2,5,8,11)
        sum_target = sum(monthly_precip[i] for i in target_months)
        print(f"Осадки по месяцам: {monthly_precip}")
        print(f"Сумма осадков в марте, июне, сентябре, декабре: {sum_target}")
        return monthly_precip

    @staticmethod
    def task_11_64():
        arr = [random.randint(-20, 30) for _ in range(12)]
        sum_positive = sum(x for x in arr if x > 0)
        sum_negative = sum(x for x in arr if x < 0)
        if sum_negative != 0:
            ratio = sum_positive / abs(sum_negative)
        else:
            ratio = float('inf')
        print(f"Массив: {arr}")
        print(f"Сумма положительных: {sum_positive}, Сумма отрицательных: {sum_negative}")
        print(f"Отношение: {ratio:.2f}")
        return arr

    @staticmethod
    def task_11_65():
        arr = [random.randint(1, 100) for _ in range(20)]
        sum_above_20 = sum(x for x in arr if x > 20)
        sum_below_50 = sum(x for x in arr if x < 50)
        condition_a = sum_above_20 > 100
        condition_b = sum_below_50 % 2 == 0
        print(f"Массив: {arr}")
        print(f"а) Сумма >20 превышает 100: {condition_a}")
        print(f"б) Сумма <50 четная: {condition_b}")
        return arr

    @staticmethod
    def task_11_66():
        feb_precip = [random.randint(0, 20) for _ in range(28)]
        sum_even_days = sum(feb_precip[i] for i in range(1, 28, 2))  # четные дни
        sum_odd_days = sum(feb_precip[i] for i in range(0, 28, 2))  # нечетные дни
        print(f"Осадки февраля: {feb_precip}")
        print(f"Сумма по четным дням: {sum_even_days}")
        print(f"Сумма по нечетным дням: {sum_odd_days}")
        print(f"По четным выпало больше: {sum_even_days > sum_odd_days}")
        return feb_precip

    @staticmethod
    def task_11_67():
        residents = [random.randint(50, 200) for _ in range(20)]
        sum_odd_houses = sum(residents[i] for i in range(0, 20, 2))  # нечетные номера
        sum_even_houses = sum(residents[i] for i in range(1, 20, 2))  # четные номера
        print(f"Жители в домах: {residents}")
        print(f"Сумма в нечетных домах: {sum_odd_houses}")
        print(f"Сумма в четных домах: {sum_even_houses}")
        print(f"Больше жителей на {'нечетной' if sum_odd_houses > sum_even_houses else 'четной'} стороне")
        return residents

    @staticmethod
    def task_11_68():
        arr = [random.randint(-10, 20) for _ in range(15)]
        count_non_negative = sum(1 for x in arr if x >= 0)
        print(f"Массив: {arr}")
        print(f"Количество неотрицательных: {count_non_negative}")
        return arr

    @staticmethod
    def task_11_69():
        int_arr = [random.randint(1, 20) for _ in range(12)]
        last_element = int_arr[-1]
        count_different = sum(1 for x in int_arr if x != last_element)
        a = 5
        count_multiples = sum(1 for x in int_arr if x % a == 0)
        print(f"Массив: {int_arr}")
        print(f"а) Отличных от последнего ({last_element}): {count_different}")
        print(f"б) Кратных {a}: {count_multiples}")
        return int_arr

    @staticmethod
    def task_11_70():
        feb_precip = [random.randint(0, 10) for _ in range(28)]
        count_dry_days = sum(1 for x in feb_precip if x == 0)
        print(f"Осадки февраля: {feb_precip}")
        print(f"Дней без осадков: {count_dry_days}")
        return feb_precip

    @staticmethod
    def task_11_71():
        chemistry_grades = [random.randint(2, 5) for _ in range(25)]
        count_failing = sum(1 for x in chemistry_grades if x == 2)
        print(f"Оценки по химии: {chemistry_grades}")
        print(f"Неуспевающих: {count_failing}")
        return chemistry_grades

    @staticmethod
    def task_11_72():
        march_sales = [random.randint(1000, 5000) for _ in range(31)]
        s = 3000
        count_above_s = sum(1 for x in march_sales if x > s)
        print(f"Продажи за март: {march_sales}")
        print(f"Дней с продажами > {s}: {count_above_s}")
        return march_sales

    @staticmethod
    def task_11_73():
        heights = [random.randint(150, 190) for _ in range(22)]
        r = 170
        count_under_r = sum(1 for x in heights if x <= r)
        print(f"Рост учеников: {heights}")
        print(f"Учеников ростом ≤ {r}: {count_under_r}")
        return heights

    @staticmethod
    def task_11_74():
        arr = [random.randint(1, 100) for _ in range(20)]
        a, b = 20, 50
        count_in_range = sum(1 for x in arr if a <= x <= b)
        print(f"Массив: {arr}")
        print(f"Элементов в промежутке [{a}, {b}]: {count_in_range}")
        return arr

    @staticmethod
    def task_11_75():
        game_results = [random.choice([0, 1, 3]) for _ in range(20)]
        wins = sum(1 for x in game_results if x == 3)
        draws = sum(1 for x in game_results if x == 1)
        print(f"Результаты 20 игр: {game_results}")
        print(f"Выигрышей: {wins}, Ничьих: {draws}")
        print(f"Общее количество выигрышей и ничьих: {wins + draws}")
        return game_results

    @staticmethod
    def task_11_76():
        grades_10 = [random.randint(2, 5) for _ in range(10)]
        count_4 = sum(1 for x in grades_10 if x == 4)
        count_5 = sum(1 for x in grades_10 if x == 5)
        print(f"Оценки по 10 предметам: {grades_10}")
        print(f"Четверок: {count_4}, Пятерок: {count_5}")
        print(f"Общее количество четверок и пятерок: {count_4 + count_5}")
        return grades_10

    @staticmethod
    def task_11_77():
        arr = [random.randint(-15, 15) for _ in range(15)]
        count_positive = sum(1 for x in arr if x > 0)
        count_negative = sum(1 for x in arr if x < 0)
        print(f"Массив: {arr}")
        print(f"Положительных: {count_positive}, Отрицательных: {count_negative}")
        return arr

    @staticmethod
    def task_11_78():
        int_arr = [random.randint(1, 100) for _ in range(20)]
        count_even = sum(1 for x in int_arr if x % 2 == 0)
        count_ends_with_5 = sum(1 for x in int_arr if x % 10 == 5)
        print(f"Массив: {int_arr}")
        print(f"Четных: {count_even}, Оканчивающихся на 5: {count_ends_with_5}")
        return int_arr

    @staticmethod
    def task_11_79():
        game_results = [random.choice([1, 2, 3]) for _ in range(20)]
        wins = sum(1 for x in game_results if x == 3)
        draws = sum(1 for x in game_results if x == 1)
        losses = sum(1 for x in game_results if x == 2)
        print(f"Результаты 20 игр: {game_results}")
        print(f"Выигрышей: {wins}, Ничьих: {draws}, Проигрышей: {losses}")
        return game_results

    @staticmethod
    def task_11_80():
        language_grades = [random.randint(2, 5) for _ in range(22)]
        count_5 = sum(1 for x in language_grades if x == 5)
        count_4 = sum(1 for x in language_grades if x == 4)
        count_3 = sum(1 for x in language_grades if x == 3)
        count_2 = sum(1 for x in language_grades if x == 2)
        print(f"Оценки по иностранному языку: {language_grades}")
        print(f"Пятерок: {count_5}, Четверок: {count_4}, Троек: {count_3}, Двоек: {count_2}")
        return language_grades


def main():
    tasks = {
        '51': ('Сумма неотрицательна', ArrayTasks1151_1180.task_11_51),
        '52': ('Проверки суммы', ArrayTasks1151_1180.task_11_52),
        '53': ('Ученики в классах', ArrayTasks1151_1180.task_11_53),
        '54': ('Книги в библиотеке', ArrayTasks1151_1180.task_11_54),
        '55': ('Грузоподъемность автомобиля', ArrayTasks1151_1180.task_11_55),
        '56': ('Спортсмен-десятиборец', ArrayTasks1151_1180.task_11_56),
        '57': ('Осадки в июне', ArrayTasks1151_1180.task_11_57),
        '58': ('Фигурное катание', ArrayTasks1151_1180.task_11_58),
        '59': ('Суммы по условиям', ArrayTasks1151_1180.task_11_59),
        '60': ('Суммы целых чисел', ArrayTasks1151_1180.task_11_60),
        '61': ('Сумма четных позиций', ArrayTasks1151_1180.task_11_61),
        '62': ('Осадки по четным числам', ArrayTasks1151_1180.task_11_62),
        '63': ('Осадки по месяцам', ArrayTasks1151_1180.task_11_63),
        '64': ('Отношение сумм', ArrayTasks1151_1180.task_11_64),
        '65': ('Проверки сумм', ArrayTasks1151_1180.task_11_65),
        '66': ('Осадки по четным/нечетным', ArrayTasks1151_1180.task_11_66),
        '67': ('Жители по сторонам улицы', ArrayTasks1151_1180.task_11_67),
        '68': ('Неотрицательные элементы', ArrayTasks1151_1180.task_11_68),
        '69': ('Подсчет элементов', ArrayTasks1151_1180.task_11_69),
        '70': ('Дни без осадков', ArrayTasks1151_1180.task_11_70),
        '71': ('Неуспевающие по химии', ArrayTasks1151_1180.task_11_71),
        '72': ('Продажи в марте', ArrayTasks1151_1180.task_11_72),
        '73': ('Ученики по росту', ArrayTasks1151_1180.task_11_73),
        '74': ('Элементы в промежутке', ArrayTasks1151_1180.task_11_74),
        '75': ('Результаты футбольных игр', ArrayTasks1151_1180.task_11_75),
        '76': ('Четверки и пятерки', ArrayTasks1151_1180.task_11_76),
        '77': ('Положительные и отрицательные', ArrayTasks1151_1180.task_11_77),
        '78': ('Четные и оканчивающиеся на 5', ArrayTasks1151_1180.task_11_78),
        '79': ('Статистика футбольных игр', ArrayTasks1151_1180.task_11_79),
        '80': ('Оценки по иностранному языку', ArrayTasks1151_1180.task_11_80),

    }
    print("=" * 70)
    print("=" * 70)
    while True:
        print("\n" + "=" * 50)
        print("ВЫБЕРИТЕ ЗАДАЧУ (11.51-11.80):")
        print("-" * 50)
        for i in range(51, 81, 5):
            group = [f"{j:2}" for j in range(i, min(i + 5, 81))]
            tasks_desc = [tasks[str(j)][0] for j in range(i, min(i + 5, 81))]
            print("  ".join(f"{num}. {desc}" for num, desc in zip(group, tasks_desc)))
        print("\n0. Выход из программы")
        print("=" * 50)
        choice = input("\nВведите номер задачи (51-80): ").strip()
        if choice == '0':
            print("\nСпасибо за использование программы! До свидания!")
            break
        if choice in tasks:
            print(f"\n{'=' * 60}")
            try:
                tasks[choice][1]()
            except Exception as e:
                print(f"Ошибка при выполнении задачи: {e}")
        else:
            print("Неверный выбор! Пожалуйста, введите число от 51 до 80.")

        input("\nНажмите Enter для продолжения...")
if __name__ == "__main__":
    main()

