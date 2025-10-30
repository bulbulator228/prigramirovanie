def days_in_month_simple():
    n = int(input("Введите номер месяца (1-12): "))
    if n == 2:
        print(28)
    elif n in (4, 6, 9, 11):
        print(30)
    else:
        print(31)