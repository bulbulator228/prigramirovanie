g, m, n = map(int, input("Введите год, месяц, число: ").split())
# Проверка високосности
def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
# Количество дней в месяце
def days_in_month(year, month):
    if month == 2:
        return 29 if is_leap(year) else 28
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days[month - 1]
# Предыдущий день
if n > 1:
    prev_day = n - 1
    prev_month = m
    prev_year = g
else:
    prev_month = m - 1
    if prev_month == 0:
        prev_month = 12
        prev_year = g - 1
    else:
        prev_year = g
    prev_day = days_in_month(prev_year, prev_month)