class ArrayTasksExtended:
    def __init__(self, arr):
        self.arr = arr

    # 11.111
    def task_11_111(self):
        """Наибольшая длина отрезка из нечетных чисел."""
        max_length = 0
        current_length = 0

        for num in self.arr:
            if num % 2 != 0:  # нечетное число
                current_length += 1
                max_length = max(max_length, current_length)
            else:
                current_length = 0

        return max_length

    # 11.112
    def task_11_112(self):
        """Анализ минимальных и максимальных элементов."""
        if not self.arr:
            return None, None, 0, None, (None, None)

        max_val = max(self.arr)
        min_val = min(self.arr)
        max_index = self.arr.index(max_val)
        min_index = self.arr.index(min_val)
        difference = max_val - min_val

        return max_val, min_val, difference, max_index, (min_index, max_index)

    # 11.113
    def task_11_113(self):
        """Количество страниц в самой толстой книге."""
        return max(self.arr) if self.arr else 0

    # 11.114
    def task_11_114(self):
        """Стоимость самого дорогого автомобиля."""
        return max(self.arr) if self.arr else 0

    # 11.115
    def task_11_115(self):
        """Стоимость самых дешевых конфет."""
        return min(self.arr) if self.arr else 0

    # 11.116
    def task_11_116(self):
        """Результат победителя гонки (минимальное время)."""
        return min(self.arr) if self.arr else 0

    # 11.117
    def task_11_117(self):
        """Разница между самым высоким и самым низким ростом."""
        if not self.arr:
            return 0
        return max(self.arr) - min(self.arr)

    # 11.118
    def task_11_118(self, current_year=2024):
        """Разница в возрасте между самым старым и самым молодым."""
        if not self.arr:
            return 0
        oldest_age = current_year - min(self.arr)  # самый старый - минимальный год рождения
        youngest_age = current_year - max(self.arr)  # самый молодой - максимальный год рождения
        return oldest_age - youngest_age

    # 11.119
    def task_11_119(self):
        """Расчет оценки спортсмена с удалением крайних оценок."""
        if len(self.arr) < 3:
            return sum(self.arr) / len(self.arr) if self.arr else 0

        sorted_arr = sorted(self.arr)
        # Удаляем одну самую низкую и одну самую высокую оценку
        trimmed = sorted_arr[1:-1]
        return sum(trimmed) / len(trimmed)

    # 11.120
    def task_11_120(self):
        """Номер самого быстрого автомобиля."""
        if not self.arr:
            return None, None

        max_speed = max(self.arr)
        first_index = self.arr.index(max_speed)
        last_index = len(self.arr) - 1 - self.arr[::-1].index(max_speed)

        return first_index + 1, last_index + 1  # +1 для порядкового номера

    # 11.121
    def task_11_121(self):
        """Дата самого дождливого дня."""
        if not self.arr:
            return None, None

        max_precip = max(self.arr)
        first_day = self.arr.index(max_precip) + 1
        last_day = len(self.arr) - self.arr[::-1].index(max_precip)

        return first_day, last_day

    # 11.122
    def task_11_122(self):
        """Номер самого дешевого вида конфет."""
        if not self.arr:
            return None, None

        min_price = min(self.arr)
        first_index = self.arr.index(min_price) + 1
        last_index = len(self.arr) - self.arr[::-1].index(min_price)

        return first_index, last_index

    # 11.123
    def task_11_123(self, current_year=2024):
        """Номер самого старшего человека."""
        if not self.arr:
            return None, None

        # Самый старый - с минимальным годом рождения
        min_year = min(self.arr)
        first_index = self.arr.index(min_year) + 1
        last_index = len(self.arr) - self.arr[::-1].index(min_year)

        return first_index, last_index

    # 11.124
    def task_11_124(self):
        """Количество максимальных и минимальных элементов."""
        if not self.arr:
            return 0, 0

        max_val = max(self.arr)
        min_val = min(self.arr)
        max_count = self.arr.count(max_val)
        min_count = self.arr.count(min_val)

        return max_count, min_count

    # 11.125
    def task_11_125(self):
        """Количество человек с самым большим ростом."""
        if not self.arr:
            return 0
        max_height = max(self.arr)
        return self.arr.count(max_height)

    # 11.126
    def task_11_126(self):
        """Количество дней с максимальным количеством осадков."""
        if not self.arr:
            return 0
        max_precip = max(self.arr)
        return self.arr.count(max_precip)

    # 11.127
    def task_11_127(self):
        """Количество самых дешевых книг."""
        if not self.arr:
            return 0
        min_price = min(self.arr)
        return self.arr.count(min_price)

    # 11.128
    def task_11_128(self):
        """Количество самых прохладных дней."""
        if not self.arr:
            return 0
        min_temp = min(self.arr)
        return self.arr.count(min_temp)

    # 11.129
    def task_11_129(self):
        """Номера всех минимальных и максимальных элементов."""
        if not self.arr:
            return [], []

        min_val = min(self.arr)
        max_val = max(self.arr)

        min_indices = [i for i, x in enumerate(self.arr) if x == min_val]
        max_indices = [i for i, x in enumerate(self.arr) if x == max_val]

        return min_indices, max_indices

    # 11.130
    def task_11_130(self):
        """Проверка условий для максимального и минимального элементов."""
        if not self.arr:
            return False, False

        max_val = max(self.arr)
        min_val = min(self.arr)

        a = max_val - min_val <= 25
        b = min_val < max_val / 2

        return a, b

    # 11.131
    def task_11_131(self):
        """Проверка, что самый тяжелый тяжелее самого легкого более чем в 2 раза."""
        if not self.arr:
            return False

        max_weight = max(self.arr)
        min_weight = min(self.arr)
        return max_weight > 2 * min_weight

    # 11.132
    def task_11_132(self):
        """Проверка разницы в численности классов."""
        if not self.arr:
            return False

        max_students = max(self.arr)
        min_students = min(self.arr)
        return max_students - min_students == 10

    # 11.133
    def task_11_133(self):
        """Что встретится раньше: максимальное или минимальное число?"""
        if not self.arr:
            return "Массив пуст"

        min_val = min(self.arr)
        max_val = max(self.arr)
        min_first_index = self.arr.index(min_val)
        max_first_index = self.arr.index(max_val)

        if min_first_index < max_first_index:
            return "Минимальное"
        elif max_first_index < min_first_index:
            return "Максимальное"
        else:
            return "Одновременно"

    # 11.134
    def task_11_134(self, current_year=2024):
        """Кто указан раньше: самый старый или самый молодой?"""
        if not self.arr:
            return "Массив пуст"

        # Переводим годы рождения в возраст
        ages = [current_year - year for year in self.arr]
        max_age = max(ages)  # самый старый
        min_age = min(ages)  # самый молодой

        oldest_index = ages.index(max_age)
        youngest_index = ages.index(min_age)

        if oldest_index < youngest_index:
            return "Самый старый"
        elif youngest_index < oldest_index:
            return "Самый молодой"
        else:
            return "Один и тот же человек"

    # 11.135
    def task_11_135(self):
        """Что было раньше: первый выигрыш или первый проигрыш?"""
        if not self.arr:
            return "Массив пуст"

        win_index = None
        loss_index = None

        for i, points in enumerate(self.arr):
            if points == 3 and win_index is None:
                win_index = i
            if points == 0 and loss_index is None:
                loss_index = i

        if win_index is None and loss_index is None:
            return "Не было ни выигрышей, ни проигрышей"
        elif win_index is None:
            return "Сначала был проигрыш"
        elif loss_index is None:
            return "Сначала был выигрыш"
        elif win_index < loss_index:
            return "Сначала был выигрыш"
        elif loss_index < win_index:
            return "Сначала был проигрыш"
        else:
            return "Одновременно"

    # 11.136
    def task_11_136(self):
        """Определение расположения жилого комплекса по розе ветров."""
        if not self.arr:
            return "Нет данных о ветре"

        from collections import Counter
        wind_counts = Counter(self.arr)

        # Находим направление с минимальной частотой
        min_direction = min(wind_counts, key=wind_counts.get)

        wind_names = {
            1: "северный", 2: "южный", 3: "восточный",
            4: "западный", 5: "северо-западный",
            6: "северо-восточный", 7: "юго-западный",
            8: "юго-восточный"
        }

        direction_name = wind_names.get(min_direction, "неизвестное")
        return f"Жилой комплекс должен быть расположен с {direction_name} стороны"

    # 11.137
    def task_11_137(self):
        """Анализ вторых максимальных и минимальных элементов."""
        if len(self.arr) < 2:
            return "Массив слишком короткий"

        # Для максимальных
        max1 = max(self.arr)
        max2 = float('-inf')
        max1_index = self.arr.index(max1)
        max2_index = -1

        # Для минимальных
        min1 = min(self.arr)
        min2 = float('inf')
        min1_index = self.arr.index(min1)
        min2_index = -1

        for i, num in enumerate(self.arr):
            # Второй максимальный
            if num > max2 and num != max1:
                max2 = num
                max2_index = i
            elif num == max1 and i != max1_index and max2 == float('-inf'):
                max2 = num
                max2_index = i

            # Второй минимальный
            if num < min2 and num != min1:
                min2 = num
                min2_index = i
            elif num == min1 and i != min1_index and min2 == float('inf'):
                min2 = num
                min2_index = i

        result = {
            'max_elements': (max1, max2),
            'min_elements': (min1, min2),
            'max_indices': (max1_index, max2_index),
            'min_indices': (min1_index, min2_index)
        }
        return result

    # 11.138
    def task_11_138(self):
        """Скорости двух самых быстрых автомобилей."""
        if len(self.arr) < 2:
            return self.arr if self.arr else []

        max1 = max(self.arr)
        max2 = float('-inf')

        for num in self.arr:
            if num > max2 and num != max1:
                max2 = num

        # Если все элементы одинаковые
        if max2 == float('-inf'):
            max2 = max1

        return max1, max2

    # 11.139
    def task_11_139(self):
        """Стоимость двух самых дорогих видов товара."""
        if len(self.arr) < 2:
            return self.arr if self.arr else []

        max1 = max(self.arr)
        max2 = float('-inf')

        for num in self.arr:
            if num > max2 and num != max1:
                max2 = num

        if max2 == float('-inf'):
            max2 = max1

        return max1, max2

    # 11.140
    def task_11_140(self):
        """Результаты спортсменов, занявших первое и второе места (минимальное время)."""
        if len(self.arr) < 2:
            return self.arr if self.arr else []

        min1 = min(self.arr)
        min2 = float('inf')

        for num in self.arr:
            if num < min2 and num != min1:
                min2 = num

        if min2 == float('inf'):
            min2 = min1

        return min1, min2


# Демонстрация работы всех задач
def demonstrate_extended_tasks():
    test_arrays = {
        "11.111": [1, 3, 5, 2, 7, 9, 11, 4, 13, 15, 17],
        "11.112": [5, 2, 8, 1, 9, 3, 8, 1],
        "11.119": [8.5, 9.0, 7.5, 8.0, 9.5, 8.0, 7.0, 9.0],
        "11.120": [180, 200, 220, 200, 190, 220, 210],
        "11.121": [5, 10, 15, 20, 15, 10, 25, 20],
        "11.123": [1990, 1985, 2000, 1985, 1995, 1980, 2005],
        "11.130": [10, 15, 20, 25, 30],
        "11.131": [50, 60, 70, 80, 90, 100],
        "11.132": [25, 30, 28, 35, 32, 20],
        "11.133": [5, 3, 8, 1, 9, 2],
        "11.134": [1990, 1985, 2000, 1995, 1980],
        "11.135": [1, 0, 3, 1, 0, 3, 1],
        "11.136": [1, 2, 1, 3, 2, 1, 4, 2, 3, 1],
        "11.137": [10, 20, 30, 20, 10, 40, 30],
        "11.138": [180, 200, 220, 190, 210, 220, 200],
        "11.139": [100, 150, 200, 120, 180, 200, 160],
        "11.140": [10.5, 10.2, 10.8, 10.1, 10.9, 10.1, 10.7]
    }

    for task_name, arr in test_arrays.items():
        print(f"\n{task_name}: {arr}")
        processor = ArrayTasksExtended(arr)

        if task_name == "11.111":
            print(f"11.111: Наибольшая длина нечетных чисел: {processor.task_11_111()}")
        elif task_name == "11.112":
            max_val, min_val, diff, max_idx, indices = processor.task_11_112()
            print(
                f"11.112: Макс: {max_val}, Мин: {min_val}, Разница: {diff}, Индекс макс: {max_idx}, Индексы: {indices}")
        elif task_name == "11.119":
            print(f"11.119: Итоговая оценка: {processor.task_11_119():.2f}")
        elif task_name == "11.120":
            first, last = processor.task_11_120()
            print(f"11.120: Первый быстрый: {first}, Последний быстрый: {last}")
        elif task_name == "11.121":
            first, last = processor.task_11_121()
            print(f"11.121: Первый дождливый: {first}, Последний дождливый: {last}")
        elif task_name == "11.123":
            first, last = processor.task_11_123()
            print(f"11.123: Первый старый: {first}, Последний старый: {last}")
        elif task_name == "11.130":
            a, b = processor.task_11_130()
            print(f"11.130: а) {a}, б) {b}")
        elif task_name == "11.131":
            print(f"11.131: Тяжелый тяжелее легкого в 2 раза: {processor.task_11_131()}")
        elif task_name == "11.132":
            print(f"11.132: Разница 10 учеников: {processor.task_11_132()}")
        elif task_name == "11.133":
            print(f"11.133: Раньше встретилось: {processor.task_11_133()}")
        elif task_name == "11.134":
            print(f"11.134: Раньше в списке: {processor.task_11_134()}")
        elif task_name == "11.135":
            print(f"11.135: {processor.task_11_135()}")
        elif task_name == "11.136":
            print(f"11.136: {processor.task_11_136()}")
        elif task_name == "11.137":
            result = processor.task_11_137()
            print(f"11.137: Макс элементы: {result['max_elements']}, Мин элементы: {result['min_elements']}")
        elif task_name == "11.138":
            print(f"11.138: Две самые быстрые скорости: {processor.task_11_138()}")
        elif task_name == "11.139":
            print(f"11.139: Два самых дорогих товара: {processor.task_11_139()}")
        elif task_name == "11.140":
            print(f"11.140: Первое и второе места: {processor.task_11_140()}")


if __name__ == "__main__":
    demonstrate_extended_tasks()