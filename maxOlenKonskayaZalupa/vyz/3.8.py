ticket_number = int(input("Введите номер билета: "))
first_ticket_num = 1643
pos = ticket_number - first_ticket_num
row = pos // 15 + 1
print("Номер ряда:", row)