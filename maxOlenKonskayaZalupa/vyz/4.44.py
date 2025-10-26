x = float(input("Введите x: "))
in_area = (float('-inf') < x < -1) or (5 < x < float('inf'))
print(f"Точка принадлежит области I или III?", in_area)