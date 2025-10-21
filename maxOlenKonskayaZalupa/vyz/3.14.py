apt_num = int(input("Номер квартиры: "))
floors = 9
porches = 4
apts_per_floor = 6
apts_per_porch = floors * apts_per_floor  # 9 * 6 =54

# 1) Номер подъезда
porch_num = (apt_num - 1) // apts_per_porch + 1

# 2) Этаж внутри подъезда
pos_in_porch = (apt_num - 1) % apts_per_porch
floor_num = pos_in_porch // apts_per_floor + 1

# 3) Номер квартиры на этаже
apt_on_floor = pos_in_porch % apts_per_floor + 1

print("Подъезд:", porch_num)
print("Этаж:", floor_num)
print("Порядковый номер квартиры на этаже:", apt_on_floor)