m, n = map(int, input("Введите месяц и число: ").split())
# Количество дней в каждом месяце не високосного года
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# Предыдущий день
if n > 1:
    prev_day = n - 1
    prev_month = m
else:
    prev_month = m - 1
    prev_day = days_in_month[prev_month - 1]
# Следующий день
if n < days_in_month[m - 1]:
    next_day = n + 1
    next_month = m
else:
    next_month = m + 1
    next_day = 1
print(f"Предыдущий день: {prev_month}.{prev_day}")
print(f"Следующий день: {next_month}.{next_day}")