monitor = float(input("Цена монитора: "))
system_unit = float(input("Цена системного блока: "))
keyboard = float(input("Цена клавиатуры: "))
mouse = float(input("Цена мыши: "))

N = int(input("Количество компьютеров: "))

price_one = monitor + system_unit + keyboard + mouse
total_price = N * price_one
print(f"Стоимость {N} компьютеров:", total_price)
