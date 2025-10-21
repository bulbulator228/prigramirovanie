apt_number = int(input("Введите номер квартиры (1-15): "))
floor = (apt_number - 1) // 3 + 1
print("Этаж квартиры:", floor)