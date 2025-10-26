t = float(input("Введите время t (в минутах от начала часа): "))
cycle_time = 5
t_mod = t % 10
if 0 <= t_mod < 3 or 5 <= t_mod < 8:
    print("Горит зелёный сигнал")
else:
    print("Горит красный сигнал")