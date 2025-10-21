n = int(input("Порядковый номер в таблице (1-50): "))
rows = 10
cols = 5
row_num = (n - 1) // cols + 1
print("Номер строки:", row_num)