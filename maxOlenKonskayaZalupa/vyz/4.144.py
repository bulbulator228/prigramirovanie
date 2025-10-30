def is_leap_year(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
def prev_next_day_leap():
    g = int(input("Введите год: "))
    m = int(input("Введите номер месяца (1-12): "))
    n = int(input("Введите число месяца: "))
    if not (1 <= m <= 12):
        print("Неверный номер месяца")
        return
    days_in_month = [31, 29 if is_leap_year(g) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if not (1 <= n <= days_in_month[m - 1]):
        print("Неверное число для данного месяца")
        return
    # Предыдущий день
    if n > 1:
        prev_m, prev_n, prev_g = m, n - 1, g
    else:
        if m == 1:
            prev_g = g - 1
            prev_m = 12
            prev_n = 31
        else:
            prev_g = g
            prev_m = m - 1
            prev_n = days_in_month[prev_m - 1]
    print(f"а) Предыдущий день: {prev_n}.{prev_m}.{prev_g}")
    # Следующий день
    if n < days_in_month[m - 1]:
        next_m, next_n, next_g = m, n + 1, g
    else:
        if m == 12:
            next_g = g + 1
            next_m = 1
            next_n = 1
        else:
            next_g = g
            next_m = m + 1
            next_n = 1
    print(f"б) Следующий день: {next_n}.{next_m}.{next_g}")