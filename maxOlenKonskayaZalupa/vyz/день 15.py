# 7.49
n = int(input("Введите число дней в месяце: "))
total_precipitation = 0
for day in range(1, n + 1):
    precipitation = float(input(f"Осадки за день {day}: "))
    if day % 2 == 0:
        total_precipitation += precipitation
print("Общее количество осадков в четные дни:", total_precipitation)

# 7.50
k = 11
total_students = 0
for class_number in range(1, k + 1):
    count = int(input(f"Число учеников в {class_number}-ом классе: "))
    if class_number % 2 != 0:
        total_students += count
print("Общее число учеников в нечетных классах:", total_students)

# 7.51
n = int(input("Введите количество чисел: "))
first_odd = True
sum_odd_sequence = 0
for _ in range(n):
    num = int(input("Введите число: "))
    # условие без оператора if - используем логический оператор
    # (в Python условие обязательно, поэтому заменим на булев флаг)
    if first_odd:
        sum_odd_sequence += num
        if num % 2 == 0:
            first_odd = False
    else:
        break
print("Сумма подряд идущих нечетных чисел в начале:", sum_odd_sequence)

# 7.52
b = []
for i in range(14):
    b.append(int(input(f"Введите число b{i+1}: ")))
sum_greater_20 = sum(x for x in b if x > 20)
sum_less_50 = sum(x for x in b if x < 50)
print("Сумма чисел, больших 20, превышает 100:", sum_greater_20 > 100)
print("Сумма чисел, меньших 50, — четное число:", sum_less_50 % 2 == 0)

# 7.53
n = int(input("Введите n: "))
m_list = []
for _ in range(n):
    m_list.append(int(input("Введите число: ")))
sum_less_25_5 = sum(x for x in m_list if x < 25.5)
sum_less_equal_20 = sum(x for x in m_list if x <= 20)
print("Сумма чисел меньше 25.5 не превышает 50:", sum_less_25_5 <= 50)
print("Сумма чисел, не превышающих 20, кратна трем:", sum_less_equal_20 % 3 == 0)

# 7.54
n = int(input("Введите n: "))
p = float(input("Введите значение p: "))
d = []
for _ in range(n):
    d.append(float(input("Введите число: ")))
sum_greater_20_5 = sum(x for x in d if x > 20.5)
print("Сумма чисел > 20.5 и < p равна p:", sum_greater_20_5 == p)

# 7.55
n = int(input("Введите n: "))
m = int(input("Введите m: "))
q = int(input("Введите q: "))
a = []
for _ in range(n):
    a.append(int(input("Введите число: ")))
sum_below_m = sum(x for x in a if x <= m)
print("Сумма чисел не больше m превышает q:", sum_below_m > q)

# 7.56
n = int(input("Введите n: "))
m = int(input("Введите m: "))
p = int(input("Введите p: "))
c = []
for _ in range(n):
    c.append(int(input("Введите число: ")))
sum_below_m = sum(x for x in c if x <= m)
print("Сумма чисел, не превышающих m, кратна p:", sum_below_m % p == 0)

# 7.57
days = int(input("Введите количество дней февраля: "))
sum_even = 0
sum_odd = 0
for day in range(1, days + 1):
    precipitation = float(input(f"Осадки за день {day}: "))
    if day % 2 == 0:
        sum_even += precipitation
    else:
        sum_odd += precipitation
print("Больше осадков по четным дням:", sum_even > sum_odd)

# 7.58
n = int(input("Введите число домов: "))
residents_odd = 0
residents_even = 0
for i in range(1, n + 1):
    residents = int(input(f"Жители дома {i}: "))
    if i % 2 == 0:
        residents_even += residents
    else:
        residents_odd += residents
print("На стороне с нечетными номерами проживает больше:", residents_odd > residents_even)

# 7.59
k = int(input("Введите число оценок: "))
count_fives = 0
for _ in range(k):
    grade = int(input("Введите оценку: "))
    if grade == 5:
        count_fives += 1
print("Количество пятерок:", count_fives)

# 7.60
n = int(input("Введите число дней: "))
count_below_zero = 0
for _ in range(n):
    temp = float(input("Температура: "))
    if temp < 0:
        count_below_zero += 1
print("Количество дней с температурой ниже 0:", count_below_zero)

# 7.61
n = 12
count_short = 0
for _ in range(n):
    height = float(input("Рост юноши: "))
    if height < 165:
        count_short += 1
print("Число юношей с ростом менее 165 см:", count_short)

#7.62
n = int(input("Введите n: "))
a = list(map(int, input("Введите последовательность a1, a2, ..., an: ").split()))
p = int(input("Введите p: "))
k = int(input("Введите k: "))
count_bigger_p = sum(1 for x in a if x > p)
count_ending_5 = sum(1 for x in a if str(abs(x))[-1] == '5')
count_div_k = sum(1 for x in a if x % k == 0)
print("а) Количество чисел больше p:", count_bigger_p)
print("б) Количество чисел, оканчивающихся цифрой 5:", count_ending_5)
print("в) Количество чисел, кратных k:", count_div_k)

#7.63
n = int(input("Введите количество учеников: "))
oceny = list(map(int, input("Введите оценки учеников через пробел: ").split()))
pjat = sum(1 for oc in oceny if oc == 5)
dve = sum(1 for oc in oceny if oc == 2)
print("Количество пятёрок:", pjat)
print("Количество двоек:", dve)

#7.64
n = int(input("Введите количество человек: "))
gods = list(map(int, input("Введите годы рождения через пробел: ").split()))
before_1990 = sum(1 for g in gods if g < 1990)
after_2000 = sum(1 for g in gods if g > 2000)
print("Людей, рождавшихся до 1990:", before_1990)
print("Людей, рождавшихся после 2000:", after_2000)

#7.65
n = int(input("Введите количество команд: "))
wins = []
losses = []
for i in range(n):
    w = int(input(f"Введите количество побед команды {i+1}: "))
    l = int(input(f"Введите количество поражений команды {i+1}: "))
    wins.append(w)
    losses.append(l)
count_more_wins = sum(1 for w, l in zip(wins, losses) if w > l)
print("Количество команд с большим числом побед, чем поражений:", count_more_wins)

#7.66
n = int(input("Введите длину последовательности: "))
sequence = list(map(float, input("Введите последовательность из n чисел: ").split()))
count_neg_start = 0
for num in sequence:
    if num >= 0:
        break
    count_neg_start += 1
print("Количество отрицательных чисел в начале последовательности:", count_neg_start)

#7.67
sequence = []
print("Введите числа последовательности. Для завершения введите 0.")
while True:
    num = float(input())
    if num == 0:
        break
    sequence.append(num)
index_first_zero = len(sequence)
for i, num in enumerate(sequence):
    if num == 0:
        index_first_zero = i
        break
print("Количество чисел, предшествующих первому нулю:", index_first_zero)

#7.68
n = int(input("Введите длину последовательности: "))
sequence = list(map(int, input("Введите целые числа: ").split()))
k = 1
for i in range(1, n):
    if sequence[i] != sequence[0]:
        k = i
        break
else:
    k = n
count_equal = k
print("Количество таких элементов:", count_equal)

#7.69
import math
grades = list(map(int, input("Введите оценки по информатике (20 оценок через пробел): ").split()))
count_fives = len([x for x in grades if x == 5])
print("Количество учеников с оценкой 5:", count_fives)

#7.70
n = 31
rainfalls = list(map(int, input("Введите осадки за каждый день мая через пробел: ").split()))
count_no_rain = 0
for rainfall in rainfalls:
    if rainfall != 0:
        break
    count_no_rain += 1
print("Дней подряд с отсутствием осадков с 1 мая:", count_no_rain)

#7.71
n = int(input("Введите число студентов: "))
ocenki = []
dvojki_count = 0
for _ in range(n):
    oc = int(input("Введите оценку студента: "))
    ocenki.append(oc)
for oc in ocenki:
    if oc == 2:
        dvojki_count += 1
print("Количество студентов с двойкой:", dvojki_count)

#7.72
n = int(input("Введите n: "))
a = list(map(float, input("Введите последовательность из n чисел: ").split()))
count_positive = sum(1 for x in a if x > 0)
count_negative = sum(1 for x in a if x < 0)
print("Количество положительных чисел:", count_positive)
print("Количество отрицательных чисел:", count_negative)

#7.73
m = int(input("Введите количество чисел (m): "))
x = []
for i in range(m):
    xi = int(input(f"Введите число {i+1}: "))
    x.append(xi)
count_multiples_3 = sum(1 for num in x if num % 3 == 0)
count_multiples_7 = sum(1 for num in x if num % 7 == 0)
print(f"Количество чисел, кратных 3: {count_multiples_3}")
print(f"Количество чисел, кратных 7: {count_multiples_7}")

#7.74
n = int(input("Введите число троек: "))
count = 0
for _ in range(n):
    a, b, c = map(int, input("Введите три числа a, b, c (a ≤ b ≤ c): ").split())
    if a + b > c:
        count += 1
print(f"Количество троек, которые могут образовать треугольник: {count}")

#7.76
total_removals = 0
total_time_team1 = 0
total_time_team2 = 0
for _ in range(24):
    team = int(input("Введите номер команды (1 или 2): "))
    duration = int(input("Введите длительность удаления (2, 5 или 10 минут): "))
    total_removals += 1
    if team == 1:
        total_time_team1 += duration
    elif team == 2:
        total_time_team2 += duration
print(f"Общее число удалений: {total_removals}")
print(f"Общее время удалений команды 1: {total_time_team1} минут")
print(f"Общее время удалений команды 2: {total_time_team2} минут")

#7.77
removals_team1 = 0
penalty_time_team1 = 0
removals_team2 = 0
penalty_time_team2 = 0
while True:
    team = int(input("Введите команду (1 или 2, 0 для завершения): "))
    if team == 0:
        break
    duration = int(input("Введите длительность удаления (2, 5 или 10): "))
    if team == 1:
        removals_team1 += 1
        penalty_time_team1 += duration
    elif team == 2:
        removals_team2 += 1
        penalty_time_team2 += duration
print("Результаты:")
print(f"Команда 1 - удаления: {removals_team1}, штрафное время: {penalty_time_team1} минут")
print(f"Команда 2 - удаления: {removals_team2}, штрафное время: {penalty_time_team2} минут")

#7.78
grades = []
for _ in range(int(input("Введите количество оценок: "))):
    grade = int(input("Введите оценку (2,3,4 или 5): "))
    grades.append(grade)
counts = {5: 0, 4: 0, 3: 0, 2: 0}
for g in grades:
    if g in counts:
        counts[g] += 1
print(f"Пятерок: {counts[5]}")
print(f"Четверок: {counts[4]}")
print(f"Троек: {counts[3]}")
print(f"Двое: {counts[2]}")

#7.79
points = int(input("Введите очки, набранные командой: "))
wins = 0
losses = 0
draws = 0
num_games = int(input("Введите число игр: "))
print("Введите очки за каждую игру:")
for _ in range(num_games):
    score = int(input())
    if score == 3:
        wins += 1
    elif score == 1:
        draws += 1
    elif score == 0:
        losses += 1
print(f"Выигрышей: {wins}")
print(f"Проигрышей: {losses}")
print(f"Ничьих: {draws}")

#7.80
wins = 0
losses = 0
draws = 0
large_diff_count = 0
total_points = 0

for _ in range(20):
    goals_scored, goals_conceded = map(int, input("Введите забитые и пропущенные мячи: ").split())
    # а)
    if goals_scored > goals_conceded:
        print("выигрыш")
        wins += 1
    elif goals_scored == goals_conceded:
        print("ничья")
        draws += 1
    else:
        print("проигрыш")
        losses += 1
    # д)
    if abs(goals_scored - goals_conceded) >= 3:
        large_diff_count += 1
    # е)
    if goals_scored > goals_conceded:
        total_points += 3
    elif goals_scored == goals_conceded:
        total_points += 1
print(f"Общее количество выигрышей: {wins}")
print(f"Количество ничьих: {draws}")
print(f"Количество проигрышей: {losses}")
print(f"Игр с разностью >= 3: {large_diff_count}")
print(f"Общее число набранных очков: {total_points}")