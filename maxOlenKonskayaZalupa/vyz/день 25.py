class ArrayTasks:
    def __init__(self, arr):
        self.arr = arr.copy() if arr else []

    # 11.141
    def task_141(self, current_year=2024):
        """Годы рождения двух самых старших людей"""
        if len(self.arr) < 2:
            return self.arr
        sorted_years = sorted(self.arr)
        return sorted_years[:2]

    # 11.142
    def task_142(self):
        """Команды, занявшие первое и второе места"""
        if len(self.arr) < 2:
            return self.arr

        max1 = max(self.arr)
        max2 = float('-inf')
        for x in self.arr:
            if x > max2 and x != max1:
                max2 = x
        if max2 == float('-inf'):
            max2 = max1
        return max1, max2

    # 11.143
    def task_143(self):
        """Даты двух самых теплых дней"""
        if len(self.arr) < 2:
            return []

        temp_days = self.arr.copy()
        max1 = max(temp_days)
        max1_index = temp_days.index(max1)

        temp_value = temp_days[max1_index]
        temp_days[max1_index] = float('-inf')

        max2 = max(temp_days)
        max2_index = temp_days.index(max2)

        temp_days[max1_index] = temp_value

        return [max1_index + 1, max2_index + 1]

    # 11.144
    def task_144(self):
        """Два этажа с наименьшим количеством жителей"""
        if len(self.arr) < 2:
            return []

        floors = []
        for i, count in enumerate(self.arr):
            floors.append((count, i + 1))

        floors.sort(key=lambda x: x[0])
        return [floors[0][1], floors[1][1]]

    # 11.145
    def task_145(self):
        """Даты двух самых холодных дней"""
        if len(self.arr) < 2:
            return []

        temp_days = self.arr.copy()
        min1 = min(temp_days)
        min1_index = temp_days.index(min1)

        temp_value = temp_days[min1_index]
        temp_days[min1_index] = float('inf')

        min2 = min(temp_days)
        min2_index = temp_days.index(min2)

        temp_days[min1_index] = temp_value

        return [min1_index + 1, min2_index + 1]

    # 11.146
    def task_146(self):
        """Команда из 4 лучших бегунов"""
        if len(self.arr) < 4:
            return "Недостаточно спортсменов"

        runners = []
        for i, time in enumerate(self.arr):
            runners.append((time, i + 1))

        runners.sort(key=lambda x: x[0])
        return [runner[1] for runner in runners[:4]]

    # 11.147
    def task_147(self):
        """Изменить знак у максимального по модулю элемента"""
        if not self.arr:
            return []

        arr_copy = self.arr.copy()
        max_abs_index = 0
        max_abs_value = abs(arr_copy[0])

        for i in range(1, len(arr_copy)):
            if abs(arr_copy[i]) > max_abs_value:
                max_abs_value = abs(arr_copy[i])
                max_abs_index = i

        arr_copy[max_abs_index] = -arr_copy[max_abs_index]
        return arr_copy

    # 11.148
    def task_148(self):
        """Однократный проход пузырьковой сортировки"""
        if len(self.arr) < 2:
            return self.arr[-1] if self.arr else None

        arr_copy = self.arr.copy()
        for i in range(len(arr_copy) - 1):
            if arr_copy[i + 1] < arr_copy[i]:
                arr_copy[i], arr_copy[i + 1] = arr_copy[i + 1], arr_copy[i]

        return arr_copy[-1]

    # 11.149
    def task_149(self, A=5):
        """Преобразования элементов массива"""
        arr_copy = self.arr.copy()

        doubled = [x * 2 for x in arr_copy]
        subtracted = [x - A for x in arr_copy]

        if arr_copy and arr_copy[0] != 0:
            divided = [x / arr_copy[0] for x in arr_copy]
        else:
            divided = arr_copy.copy()

        return doubled, subtracted, divided

    # 11.150
    def task_150(self, B=10):
        """Преобразования элементов массива"""
        arr_copy = self.arr.copy()

        minus_20 = [x - 20 for x in arr_copy]

        if arr_copy:
            last_element = arr_copy[-1]
            multiplied = [x * last_element for x in arr_copy]
        else:
            multiplied = arr_copy.copy()

        plus_B = [x + B for x in arr_copy]

        return minus_20, multiplied, plus_B

    # 11.151
    def task_151(self, m=1, n=4):
        """Перестановка элементов"""
        arr_copy = self.arr.copy()
        results = {}

        if len(arr_copy) >= 5:
            arr_a = arr_copy.copy()
            arr_a[1], arr_a[4] = arr_a[4], arr_a[1]
            results['a'] = arr_a
        else:
            results['a'] = "Недостаточно элементов"

        if (0 <= m < len(arr_copy) and 0 <= n < len(arr_copy) and
                m != n and len(arr_copy) > max(m, n)):
            arr_b = arr_copy.copy()
            arr_b[m], arr_b[n] = arr_b[n], arr_b[m]
            results['b'] = arr_b
        else:
            results['b'] = "Некорректные индексы"

        if len(arr_copy) >= 3:
            arr_c = arr_copy.copy()
            max_val = max(arr_c)
            max_index = arr_c.index(max_val)
            arr_c[2], arr_c[max_index] = arr_c[max_index], arr_c[2]
            results['c'] = arr_c
        else:
            results['c'] = "Недостаточно элементов"

        if arr_copy:
            arr_d = arr_copy.copy()
            min_val = min(arr_d)
            for i in range(len(arr_d) - 1, -1, -1):
                if arr_d[i] == min_val:
                    min_index = i
                    break
            arr_d[0], arr_d[min_index] = arr_d[min_index], arr_d[0]
            results['d'] = arr_d
        else:
            results['d'] = "Массив пуст"

        return results

    # 11.152
    def task_152(self):
        """Перестановки в массиве с четным числом элементов"""
        if len(self.arr) % 2 != 0:
            return {"error": "Массив должен иметь четное число элементов"}

        arr_copy = self.arr.copy()
        n = len(arr_copy)
        half = n // 2

        results = {}

        arr_a = arr_copy[half:] + arr_copy[:half]
        results['a'] = arr_a

        arr_b = []
        for i in range(0, n, 2):
            if i + 1 < n:
                arr_b.extend([arr_copy[i + 1], arr_copy[i]])
        results['b'] = arr_b

        arr_c = []
        for i in range(half):
            arr_c.append(arr_copy[half + i])
            arr_c.append(arr_copy[i])
        results['c'] = arr_c

        return results

    # 11.153
    def task_153(self):
        """Переставить первые три и последние три элемента"""
        if len(self.arr) < 6:
            return "Недостаточно элементов (нужно минимум 6)"

        arr_copy = self.arr.copy()
        result = arr_copy[-3:] + arr_copy[3:-3] + arr_copy[:3]
        return result

    # 11.154
    def task_154(self, k=1, s=9):
        """Перестановка элементов в обратном порядке"""
        arr_copy = self.arr.copy()
        results = {}

        if len(arr_copy) >= 10:
            arr_a = arr_copy.copy()
            segment = arr_a[2:10]
            arr_a[2:10] = segment[::-1]
            results['a'] = arr_a
        else:
            results['a'] = "Недостаточно элементов"

        if (0 <= k < s < len(arr_copy) and s - k > 1):
            arr_b = arr_copy.copy()
            segment = arr_b[k + 1:s]
            arr_b[k + 1:s] = segment[::-1]
            results['b'] = arr_b
        else:
            results['b'] = "Некорректные индексы"

        if len(arr_copy) >= 2:
            arr_c = arr_copy.copy()
            min_index = arr_c.index(min(arr_c))
            max_index = arr_c.index(max(arr_c))
            start, end = min(min_index, max_index), max(min_index, max_index)

            if end - start > 0:
                segment = arr_c[start:end + 1]
                arr_c[start:end + 1] = segment[::-1]

            results['c'] = arr_c
        else:
            results['c'] = "Недостаточно элементов"

        return results

    # 11.155
    def task_155(self):
        """Поменять местами первый отрицательный и последний положительный"""
        arr_copy = self.arr.copy()

        first_neg_index = None
        for i in range(len(arr_copy)):
            if arr_copy[i] < 0:
                first_neg_index = i
                break

        last_pos_index = None
        for i in range(len(arr_copy) - 1, -1, -1):
            if arr_copy[i] > 0:
                last_pos_index = i
                break

        if first_neg_index is not None and last_pos_index is not None:
            arr_copy[first_neg_index], arr_copy[last_pos_index] = \
                arr_copy[last_pos_index], arr_copy[first_neg_index]

        return arr_copy

    # 11.156 - Удаление элементов
    def delete_element(self, index):
        """Удаление элемента по индексу"""
        if not self.arr or index < 0 or index >= len(self.arr):
            return self.arr.copy() if self.arr else []

        arr_copy = self.arr.copy()
        for i in range(index, len(arr_copy) - 1):
            arr_copy[i] = arr_copy[i + 1]
        arr_copy[-1] = 0
        return arr_copy

    def task_156(self, k=2):
        """Удаление элементов по индексу"""
        results = {}
        results['a'] = self.delete_element(2)
        results['b'] = self.delete_element(k)
        return results

    # 11.157
    def task_157(self, n=5):
        """Удаление товара по индексу"""
        if 0 <= n < len(self.arr):
            return self.delete_element(n)
        else:
            return "Неверный индекс товара"

    # 11.158
    def task_158(self):
        """Удаление максимального и минимального элементов"""
        if not self.arr:
            return [], []

        arr_copy = self.arr.copy()

        max_index = arr_copy.index(max(arr_copy))
        arr_no_max = self.delete_element(max_index)

        min_index = arr_copy.index(min(arr_copy))
        arr_no_min = self.delete_element(min_index)

        return arr_no_max, arr_no_min

    # 11.159
    def task_159(self, student_index=None, student_height=None):
        """Удаление ученика из упорядоченного массива"""
        if not self.arr:
            return []

        arr_copy = self.arr.copy()

        if arr_copy != sorted(arr_copy, reverse=True):
            return "Массив должен быть упорядочен по убыванию роста"

        if student_index is not None:
            if 0 <= student_index < len(arr_copy):
                return self.delete_element(student_index)
            else:
                return "Некорректный индекс ученика"

        elif student_height is not None:
            if student_height in arr_copy:
                height_index = arr_copy.index(student_height)
                return self.delete_element(height_index)
            else:
                return "Ученик с таким ростом не найден"

        else:
            return "Не указаны данные об ученике"

    # 11.160
    def task_160(self):
        """Удаление первого отрицательного и последнего четного"""
        arr_copy = self.arr.copy()
        results = {}

        first_neg_index = None
        for i in range(len(arr_copy)):
            if arr_copy[i] < 0:
                first_neg_index = i
                break

        if first_neg_index is not None:
            results['a'] = self.delete_element(first_neg_index)
        else:
            results['a'] = "Отрицательных элементов нет"

        last_even_index = None
        for i in range(len(arr_copy) - 1, -1, -1):
            if arr_copy[i] % 2 == 0:
                last_even_index = i
                break

        if last_even_index is not None:
            results['b'] = self.delete_element(last_even_index)
        else:
            results['b'] = "Четных элементов нет"

        return results

    # 11.161
    def task_161(self):
        """Удаление максимального и минимального элементов"""
        if len(self.arr) < 2:
            return "Недостаточно элементов"

        arr_copy = self.arr.copy()

        max_index = arr_copy.index(max(arr_copy))
        arr_no_max = self.delete_element(max_index)

        processor_no_max = ArrayTasks(arr_no_max[:-1])

        if processor_no_max.arr:
            min_index = processor_no_max.arr.index(min(processor_no_max.arr))
            result = processor_no_max.delete_element(min_index)
            return result
        else:
            return arr_no_max

    # 11.162
    def task_162(self, indices=None, heights=None):
        """Удаление двух учеников из упорядоченного массива"""
        if not self.arr:
            return []

        arr_copy = self.arr.copy()

        if arr_copy != sorted(arr_copy, reverse=True):
            return "Массив должен быть упорядочен по убыванию роста"

        if indices is not None and len(indices) == 2:
            indices_sorted = sorted(indices, reverse=True)
            result = arr_copy
            for idx in indices_sorted:
                if 0 <= idx < len(result):
                    result = self._delete_from_array(result, idx)
            return result

        elif heights is not None and len(heights) == 2:
            result = arr_copy.copy()
            for height in heights:
                if height in result:
                    height_index = result.index(height)
                    result = self._delete_from_array(result, height_index)
            return result

        else:
            return "Не указаны данные об учениках"

    def _delete_from_array(self, array, index):
        """Вспомогательный метод для удаления элемента"""
        if not array or index < 0 or index >= len(array):
            return array

        result = array.copy()
        for i in range(index, len(result) - 1):
            result[i] = result[i + 1]
        result[-1] = 0
        return result

    # 11.163
    def task_163(self, n=0, n1=0, n2=0):
        """Удаление элементов по различным условиям"""
        arr_copy = self.arr.copy()
        results = {}

        arr_a = []
        for x in arr_copy:
            if x >= 0:
                arr_a.append(x)
        while len(arr_a) < len(arr_copy):
            arr_a.append(0)
        results['a'] = arr_a

        arr_b = []
        for x in arr_copy:
            if x <= n:
                arr_b.append(x)
        while len(arr_b) < len(arr_copy):
            arr_b.append(0)
        results['b'] = arr_b

        if 0 <= n1 <= n2 < len(arr_copy):
            arr_c = arr_copy.copy()
            count_to_delete = n2 - n1 + 1
            for i in range(n1, len(arr_c) - count_to_delete):
                arr_c[i] = arr_c[i + count_to_delete]
            for i in range(len(arr_c) - count_to_delete, len(arr_c)):
                arr_c[i] = 0
            results['c'] = arr_c
        else:
            results['c'] = "Некорректные индексы n1, n2"

        return results

    # 11.164
    def task_164(self):
        """Удаление элементов по сложным условиям"""
        arr_copy = self.arr.copy()
        results = {}

        arr_a = []
        for i, x in enumerate(arr_copy):
            if not (x % 2 == 0 and (i + 1) % 2 == 1):
                arr_a.append(x)
        while len(arr_a) < len(arr_copy):
            arr_a.append(0)
        results['a'] = arr_a

        arr_b = []
        for x in arr_copy:
            if x % 3 != 0 and x % 5 != 0:
                arr_b.append(x)
        while len(arr_b) < len(arr_copy):
            arr_b.append(0)
        results['b'] = arr_b

        return results

    # 11.165
    def task_165(self):
        """Удаление повторяющихся элементов, оставив первые вхождения"""
        if not self.arr:
            return []

        arr_copy = self.arr.copy()
        seen = set()
        result = []

        for x in arr_copy:
            if x not in seen:
                result.append(x)
                seen.add(x)

        while len(result) < len(arr_copy):
            result.append(0)

        return result

    # 11.166-11.170 - Вставка элементов
    def insert_after(self, index, value):
        """Вставка элемента после указанного индекса"""
        if not self.arr:
            return [value]

        arr_copy = self.arr.copy()
        arr_copy.insert(index + 1, value)
        return arr_copy

    def task_166(self, m=2):
        """Вставка чисел в массив"""
        results = {}

        if len(self.arr) >= 2:
            results['a'] = self.insert_after(1, 10)
        else:
            results['a'] = "Недостаточно элементов"

        if len(self.arr) > m:
            results['b'] = self.insert_after(m, 100)
        else:
            results['b'] = "Недостаточно элементов"

        return results

    def task_167(self, number=50):
        """Вставка после первого отрицательного и перед последним четным"""
        arr_copy = self.arr.copy()
        results = {}

        first_neg_index = None
        for i in range(len(arr_copy)):
            if arr_copy[i] < 0:
                first_neg_index = i
                break

        if first_neg_index is not None:
            results['a'] = self.insert_after(first_neg_index, number)
        else:
            results['a'] = "Отрицательных элементов нет"

        last_even_index = None
        for i in range(len(arr_copy) - 1, -1, -1):
            if arr_copy[i] % 2 == 0:
                last_even_index = i
                break

        if last_even_index is not None:
            arr_b = arr_copy.copy()
            arr_b.insert(last_even_index, number)
            results['b'] = arr_b
        else:
            results['b'] = "Четных элементов нет"

        return results

    # 11.168
    def task_168(self, new_height, position):
        """Вставка информации о новой горной вершине"""
        if not self.arr:
            return [new_height]

        if 0 <= position <= len(self.arr):
            arr_copy = self.arr.copy()
            arr_copy.insert(position, new_height)
            return arr_copy
        else:
            return "Некорректная позиция"

    # 11.169
    def task_169(self, new_height=None, position=None):
        """Вставка нового ученика в упорядоченный массив"""
        if not self.arr:
            return [new_height] if new_height is not None else []

        if self.arr != sorted(self.arr, reverse=True):
            return "Массив должен быть упорядочен по убыванию роста"

        arr_copy = self.arr.copy()

        if position is not None:
            if 0 <= position <= len(arr_copy):
                arr_copy.insert(position, new_height)
                return arr_copy
            else:
                return "Некорректная позиция"

        elif new_height is not None:
            # Находим правильную позицию для вставки
            for i in range(len(arr_copy)):
                if new_height > arr_copy[i]:
                    arr_copy.insert(i, new_height)
                    return arr_copy
            arr_copy.append(new_height)
            return arr_copy

        else:
            return "Не указаны данные о новом ученике"

    # 11.170
    def task_170(self, num1=100, num2=200):
        """Вставка двух чисел вокруг максимального элемента"""
        if not self.arr:
            return []

        arr_copy = self.arr.copy()
        max_index = arr_copy.index(max(arr_copy))

        # Вставляем первое число после любого максимального
        arr_with_first = arr_copy.copy()
        arr_with_first.insert(max_index + 1, num1)

        # Вставляем второе число перед максимальным
        arr_with_second = arr_copy.copy()
        arr_with_second.insert(max_index, num2)

        return arr_with_first, arr_with_second


# Тестирование всех задач
def test_all_tasks_141_170():
    print("=== ТЕСТИРОВАНИЕ ЗАДАЧ 11.141-11.170 ===\n")

    test_cases = [
        # 11.141-11.146
        ("11.141 - Два самых старших", [1990, 1985, 2000, 1980, 1995], {}),
        ("11.142 - Первое и второе места", [45, 38, 42, 38, 40, 42], {}),
        ("11.143 - Два самых теплых дня", [25, 28, 30, 26, 29, 27, 31], {}),
        ("11.144 - Два наименее населенных этажа", [50, 45, 60, 35, 55, 40, 65], {}),
        ("11.145 - Два самых холодных дня", [15, 18, 10, 16, 19, 17, 11], {}),
        ("11.146 - Четыре лучших бегуна", [10.5, 10.2, 10.8, 10.1, 10.9, 10.3], {}),

        # 11.147-11.155
        ("11.147 - Изменить знак макс по модулю", [5, -8, 3, 12, -15, 7], {}),
        ("11.148 - Последний элемент после прохода", [5, 3, 8, 1, 9, 2], {}),
        ("11.149 - Преобразования элементов", [2, 4, 6, 8, 10], {'A': 3}),
        ("11.151 - Перестановки элементов", [1, 2, 3, 4, 5, 6, 7], {'m': 1, 'n': 4}),
        ("11.152 - Перестановки в четном массиве", [1, 2, 3, 4, 5, 6], {}),
        ("11.155 - Обмен отриц. и полож.", [1, -2, 3, -4, 5, -6, 7], {}),

        # 11.156-11.165
        ("11.156 - Удаление элементов", [10, 20, 30, 40, 50], {'k': 1}),
        ("11.158 - Удаление макс и мин", [5, 2, 8, 1, 9, 3], {}),
        ("11.159 - Удаление ученика по индексу", [180, 175, 170, 165], {'student_index': 1}),
        ("11.160 - Удаление по условиям", [1, -2, 3, 4, -5], {}),
        ("11.165 - Удаление дубликатов", [1, 2, 2, 3, 1, 4], {}),

        # 11.166-11.170
        ("11.166 - Вставка элементов", [1, 2, 3, 4, 5], {'m': 2}),
        ("11.167 - Вставка по условию", [1, -3, 5, 2, -7, 4, 6], {'number': 99}),
        ("11.169 - Вставка ученика", [180, 175, 170, 165], {'new_height': 172}),
    ]

    for test_name, test_arr, params in test_cases:
        print(f"\n{test_name}")
        print(f"Исходный массив: {test_arr}")

        processor = ArrayTasks(test_arr)

        # Определяем метод по номеру задачи
        task_number = test_name.split(' - ')[0]
        if "11.141" in task_number:
            result = processor.task_141(**params)
        elif "11.142" in task_number:
            result = processor.task_142(**params)
        elif "11.143" in task_number:
            result = processor.task_143(**params)
        elif "11.144" in task_number:
            result = processor.task_144(**params)
        elif "11.145" in task_number:
            result = processor.task_145(**params)
        elif "11.146" in task_number:
            result = processor.task_146(**params)
        elif "11.147" in task_number:
            result = processor.task_147(**params)
        elif "11.148" in task_number:
            result = processor.task_148(**params)
        elif "11.149" in task_number:
            result = processor.task_149(**params)
        elif "11.151" in task_number:
            result = processor.task_151(**params)
        elif "11.152" in task_number:
            result = processor.task_152(**params)
        elif "11.155" in task_number:
            result = processor.task_155(**params)
        elif "11.156" in task_number:
            result = processor.task_156(**params)
        elif "11.158" in task_number:
            result = processor.task_158(**params)
        elif "11.159" in task_number:
            result = processor.task_159(**params)
        elif "11.160" in task_number:
            result = processor.task_160(**params)
        elif "11.165" in task_number:
            result = processor.task_165(**params)
        elif "11.166" in task_number:
            result = processor.task_166(**params)
        elif "11.167" in task_number:
            result = processor.task_167(**params)
        elif "11.169" in task_number:
            result = processor.task_169(**params)

        print(f"Результат: {result}")
        print("-" * 50)


if __name__ == "__main__":
    test_all_tasks_141_170()