def season_by_month():
    n = int(input("Введите номер месяца (1-12): "))
    if 1 <= n <= 12:
        if n in (12, 1, 2):
            print("зима")
        elif n in (3, 4, 5):
            print("весна")
        elif n in (6, 7, 8):
            print("лето")
        else:
            print("осень")
    else:
        print("Неверный номер месяца")