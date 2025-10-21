#1) Этаж квартиры
apt_num = int(input("Номер квартиры (1-20): "))
apt_per_floor = 4
floor = (apt_num - 1) // apt_per_floor + 1
print("Этаж:", floor)

# 2) Порядковый номер квартиры на этаже
apt_on_floor = (apt_num - 1) % apt_per_floor + 1
print("Порядковый номер квартиры на этаже:", apt_on_floor)