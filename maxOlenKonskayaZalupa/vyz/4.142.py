def month_name_after_n_months():
    n = int(input("Введите количество прошедших месяцев (n): "))
    if n < 0:
        print("Неверное количество месяцев")
        return
    months = ["январь", "февраль", "март", "апрель", "май", "июнь",
              "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days = 2
    month_index = n % 12
    if total_days > days_in_month[month_index]:
        # Переходим в следующий месяц
        month_index = (month_index + 1) % 12
    print("Месяц этого дня:", months[month_index])