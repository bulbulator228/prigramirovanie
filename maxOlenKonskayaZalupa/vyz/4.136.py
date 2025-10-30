def is_leap_year(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

def days_in_month():
    n = int(input("Введите номер месяца (1-12): "))
    if not (1 <= n <= 12):
        print("Неверный номер месяца")
        return
    leap = input("Год високосный? (да/нет): ").strip().lower()
    year = None
    if leap == "да":
        year = int(input("Введите год: "))
    days_in_month_non_leap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = days_in_month_non_leap[n-1]
    if year is not None and n == 2 and is_leap_year(year):
        days = 29
    print(days)