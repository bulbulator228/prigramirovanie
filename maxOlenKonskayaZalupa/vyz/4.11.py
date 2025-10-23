v_kmh = float(input("Введите скорость в км/ч: "))
v_ms = float(input("Введите скорость в м/с: "))
v_kmh_ms = v_kmh * 5 / 18
if v_kmh_ms > v_ms:
    print("Большая скорость: км/ч")
else:
    print("Большая скорость: м/с")
