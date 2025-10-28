t = float(input("Введите время в минутах с начала часа: "))
cycle = t % 9
if cycle < 3:
    print("Зеленый")
elif cycle < 4:
    print("Желтый")
else:
    print("Красный")