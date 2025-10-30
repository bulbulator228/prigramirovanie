def prev_next_day():
    m = int(input("Введите номер месяца (1-12): "))
    n = int(input("Введите число месяца: "))
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if not (1 <= m <= 12) or not (1 <= n <= days_in_month[m - 1]):
        print("Неверная дата")
        return
        # Предыдущий день
    if n > 1:
        prev_m, prev_n = m, n - 1
    else:
        # не 1 января, значит m > 1
        prev_m = m - 1
        prev_n = days_in_month[prev_m - 1]
    print(f"а) Предыдущий день: {prev_n}.{prev_m}")
    # Следующий день
    if n < days_in_month[m - 1]:
        next_m, next_n = m, n + 1
    else:
        # не 31 декабря, значит m < 12
        next_m = m + 1
        next_n = 1
    print(f"б) Следующий день: {next_n}.{next_m}")