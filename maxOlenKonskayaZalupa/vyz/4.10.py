km = float(input("Введите расстояние в километрах: "))
feet = float(input("Введите расстояние в футах: "))
feet_m = feet * 0.3048
km_m = km * 1000
if km_m < feet_m:
    print("Меньшее расстояние: километры")
else:
    print("Меньшее расстояние: футы")
