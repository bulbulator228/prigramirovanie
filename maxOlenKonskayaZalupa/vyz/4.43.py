x = float(input("Введите x: "))
y = float(input("Введите y: "))
in_area = (3 < x < float('inf')) and (2 < y < float('inf'))
if x ==3:
    print(' x лежит на границе')
if y ==2:
    print('y лежит на границе')
print(f"Точка принадлежит области I?", in_area)