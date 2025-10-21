seat_number = int(input("Введите номер места (1-36): "))
coupe_number = (seat_number - 1) // 4 + 1
print("Номер купе:", coupe_number)
