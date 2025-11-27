#11.171
n = int(input("Введите размер массива: "))
arr = list(map(int, input("Введите элементы массива через пробел: ").split()))
a = int(input("Введите число a: "))

#а)

new_arr_a = []
for elem in arr:
    if elem % a == 0:
        new_arr_a.append(a)
    new_arr_a.append(elem)
print("Массив после вставки перед кратными a:", new_arr_a)

#б)

new_arr_b = []
for elem in arr:
    new_arr_b.append(elem)
    if elem < 0:
        new_arr_b.append(a)
print("Массив после вставки после отрицательных элементов:", new_arr_b)

#11.172
n = int(input("Введите число n: "))
m = int(input("Введите число m: "))
size = int(input("Введите размер исходного массива: "))
arr = list(map(int, input("Введите элементы массива через пробел: ").split()))

arr_n = []
for elem in arr:
    if elem > n:
        arr_n.append(n)
    arr_n.append(elem)

arr_m = []
for elem in arr_n:
    arr_m.append(elem)
    if elem < m:
        arr_m.append(m)
print("Результирующий массив:", arr_m)

#11.173
size = 25
heights = list(map(float, input("Введите рост 25 учеников через пробел: ").split()))
pos1 = int(input("Введите позицию первого нового ученика: "))
pos2 = int(input("Введите позицию второго нового ученика: "))
height_new1 = float(input("Введите рост первого нового ученика: "))
height_new2 = float(input("Введите рост второго нового ученика: "))
heights.insert(pos1 - 1, height_new1)
if pos2 >= pos1:
    pos2 += 1
heights.insert(pos2 - 1, height_new2)
print("Обновлённый массив:", heights)
size = 25
heights = list(map(float, input("Введите рост 25 учеников через пробел: ").split()))
height_new1 = float(input("Введите рост первого нового ученика: "))
height_new2 = float(input("Введите рост второго нового ученика: "))
heights.append(height_new1)
heights.append(height_new2)
heights.sort(reverse=True)

print("Обновлённый массив:", heights)

#11.174
a = int(input("Введите число a для вставки: "))
size = int(input("Введите размер массива: "))
arr = list(map(int, input("Введите элементы массива через пробел: ").split()))
new_arr = []
for elem in arr:
    new_arr.append(elem)
    if '5' in str(abs(elem)):
        new_arr.append(a)
print("Результирующий массив:", new_arr)

#11.175
n = int(input("Введите число n для вставки: "))
size = int(input("Введите размер массива: "))
arr = list(map(int, input("Введите элементы массива через пробел: ").split()))
new_arr = []
for i in range(len(arr)-1):
    new_arr.append(arr[i])
    if arr[i] * arr[i+1] > 0:
        new_arr.append(n)
new_arr.append(arr[-1])
print("Результирующий массив:", new_arr)

#11.176
size = int(input("Введите размер массива: "))
arr = list(map(int, input("Введите элементы массива через пробел: ").split()))
if size > 0:
    first_elem = arr.pop(0)
    arr.append(first_elem)
print("Массив после перестановки:", arr)

#11.177
size = int(input("Введите размер массива: "))
arr = list(map(int, input("Введите элементы массива через пробел: ").split()))
k = int(input("Введите k: "))
if 1 <= k <= size:
    first_elem = arr.pop(0)
    arr.insert(k-1, first_elem)
print("Массив после перестановки:", arr)

#11.178
size = int(input("Введите размер массива: "))
arr = list(map(int, input("Введите элементы массива через пробел: ").split()))
s = int(input("Введите s: "))
k = int(input("Введите k: "))
if 1 <= s <= size and 1 <= k <= size and s < k:
    elem = arr.pop(s - 1)
    arr.insert(k - 1, elem)
print("Массив после перестановки:", arr)

#11.179
size = 25
arr = list(map(int, input("Введите результаты 25 спортсменов через пробел: ").split()))
if arr[0] < arr[1]:
    arr.sort(reverse=True)
print("Обновлённый упорядоченный массив:", arr)

#11.180
size = int(input("Введите размер массива: "))
arr = list(map(int, input("Введите элементы массива через пробел: ").split()))
if size > 0:
    last_elem = arr.pop()
    arr.insert(0, last_elem)
print("Массив после перестановки:", arr)

#11.181
size = int(input("Введите размер массива: "))
arr = list(map(int, input("Введите элементы массива через пробел: ").split()))
k = int(input("Введите k: "))
if 1 <= k <= size:
    last_elem = arr.pop()
    arr.insert(k - 1, last_elem)
print("Массив после перестановки:", arr)

#11.182
size = int(input("Введите размер массива: "))
arr = list(map(int, input("Введите элементы массива через пробел: ").split()))
s = int(input("Введите s: "))
k = int(input("Введите k: "))
if 1 <= s <= size and 1 <= k <= size and s > k:
    elem = arr.pop(s - 1)
    arr.insert(k - 1, elem)
print("Массив после перестановки:", arr)

def sort_array(arr):
    n = len(arr)
    last = arr[-1]
    i = n - 2
    while i >= 0 and arr[i] > last:
        arr[i + 1] = arr[i]
        i -= 1
    arr[i + 1] = last
    return arr

#11.183
arr_size = 30
print(f"Введите {arr_size} элементов массива (через пробел):")
arr = list(map(int, input().split()))
arr_sorted = sorted(arr)
print("Массив после сортировки (задача 11.183):")
print(arr_sorted)

#11.184
k_index = int(input("Введите индекс элемента k (от 0 до 29): "))
arr[k_index] = int(input(f"Введите новое значение для элемента {k_index}: "))
arr_sorted_k = sorted(arr)
print("Массив после сортировки (задача 11.184):")
print(arr_sorted_k)

#11.185
k = int(input("Введите значение k (от 0 до 27): "))
m = []
print("Введите 28 элементов массива m через пробел:")
m = list(map(int, input().split()))
m = m[k:] + m[:k]
print("Массив после переноса первых k элементов в конец:")
print(m)

#11.186
m12 = []
print("Введите 12 элементов массива m:")
m12 = list(map(int, input().split()))
new_arr = [m12[0], m12[-1], m12[1], m12[-2], m12[2], m12[-3], m12[3], m12[-4], m12[4], m12[-5], m12[5], m12[-6]]
print("Переставленный массив:")
print(new_arr)

# 11.187
lst = []
print("Введите элементы списка:")
lst = list(map(int, input().split()))

#11.187 a
lst = [100] + lst
print("После вставки 100 в начало:", lst)

#11.187
num = int(input("Введите число для вставки в начало: "))
lst = [num] + lst
print("После вставки заданного числа в начало:", lst)

#11.187 в)
index = int(input("Введите индекс для вставки перед ним: "))
num2 = int(input("Введите число для вставки: "))
lst = lst[:index] + [num2] + lst[index:]
print(f"После вставки числа {num2} перед индексом {index}:", lst)

#11.188
last_elem = lst[-1]
lst = [last_elem] + lst[:-1]
print("Список после циклического правого сдвига:", lst)

#11.189
array_5 = list(map(int, input("Введите массив для поиска элементов равных 5 через пробел: ").split()))
first_index = next((i for i, v in enumerate(array_5) if v == 5), -1)
last_index = next((i for i, v in reversed(list(enumerate(array_5))) if v == 5), -1)
print(f"номер первого элемента равного 5: {first_index}")
print(f"номер последнего элемента равного 5: {last_index}")

#11.190
array_gt_65530 = list(map(int, input("Введите массив для поиска элементов > 65530 через пробел: ").split()))
first_gt_index = next((i for i, v in enumerate(array_gt_65530) if v > 65530), -1)
last_gt_index = next((i for i, v in reversed(list(enumerate(array_gt_65530))) if v > 65530), -1)
print(f"номер первого элемента > 65530: {first_gt_index}")
print(f"номер последнего элемента > 65530: {last_gt_index}")

#11.191
array_zero = list(map(int, input("Введите массив для поиска нулевых элементов через пробел: ").split()))
zero_indices = [i for i, v in enumerate(array_zero) if v == 0]
if len(zero_indices) > 1:
    print("Все элементы, кроме первого нулевого:", [array_zero[i] for i in zero_indices[1:]])
if len(zero_indices) > 1:
    print("Все элементы, кроме последнего нулевого:", [array_zero[i] for i in zero_indices[:-1]])

#11.193
heights = list(map(int, input("Рост 15 учеников (по убыванию) через пробел: ").split()))
new_height = int(input("Рост нового ученика: "))
place = sum([h > new_height for h in heights]) + 1
print("Место нового ученика:", place)

#11.194
scores = list(map(int, input("Очки 20 команд (по убыванию): ").split()))
n = int(input("Очки искомой команды: "))
place = scores.index(n) + 1  # Индекс с +1 — это место
print("Место команды:", place)

#11.195

arr = list(map(int, input("Массив: ").split()))
first = arr[0]
from itertools import takewhile
equal_prefix = list(takewhile(lambda x: x == first, arr))
count_equal = len(equal_prefix)
rest = arr[count_equal:]
print("Количество одинаковых в начале:", count_equal)
print("Элементы после них:", *rest)

#11.196

grades = list(map(int, input("Оценки 24 учеников: ").split()))
fives = list(takewhile(lambda x: x == 5, grades))
print("Количество пятёрок:", len(fives))

#11.197

arr = list(map(int, input("Массив: ").split()))
n = int(input("Значение n: "))

# а
indices_n = [i for i, x in enumerate(arr) if x == n]
cut_a = arr[:indices_n[0]] if indices_n else arr
print("а) Элементы перед первым n:", *cut_a)

# б
indices_7 = [i for i, x in enumerate(arr) if str(abs(x))[-1] == '7']
cut_b = arr[indices_7[-1]+1:] if indices_7 else []
print("б) Элементы после последнего с концом на 7:", *cut_b)

#11.198

arr = list(map(int, input("Массив: ").split()))

# а)
odd_indices = [i for i, x in enumerate(arr) if x % 2 == 1]
print("а) Номер первого нечётного:", (odd_indices[0]+1) if odd_indices else "Нечётных нет")

# б)
div_13_indices = [i for i, x in enumerate(arr) if x % 13 == 0]
print("б) Номер первого кратного 13:", (div_13_indices[0]+1) if div_13_indices else "Нет элементов, кратных 13")

#11.199

arr = list(map(float, input("Массив вещественных чисел: ").split()))
neg_indices = [i for i, x in enumerate(arr) if x < 0]
if neg_indices:
    first_neg = neg_indices[0]
    last_neg = neg_indices[-1]
    print("а) Номер первого отрицательного:", first_neg+1)
    print("   Все после него:", *arr[first_neg+1:])
    print("б) Номер последнего отрицательного:", last_neg+1)
    print("   Все перед ним:", *arr[:last_neg])
else:
    print("Отрицательных чисел нет")

#11.200

grades = list(map(int, input("Оценки 28 учеников: ").split()))
exist_two = any([x == 2 for x in grades])
print("Двойки есть" if exist_two else "Двоек нет")
