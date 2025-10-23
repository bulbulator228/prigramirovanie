mass1 = float(input("Введите массу первого тела: "))
volume1 = float(input("Введите объём первого тела: "))
mass2 = float(input("Введите массу второго тела: "))
volume2 = float(input("Введите объём второго тела: "))
density1 = mass1 / volume1
density2 = mass2 / volume2
if density1 > density2:
    print("Плотность первого материала больше")
else:
    print("Плотность второго материала больше")
