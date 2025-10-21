N = int(input("Количество школьников: "))
k = int(input("Количество яблок: "))
apples_per_student = k // N
apples_left = k % N
print("Яблок на каждого:", apples_per_student)
print("Остаток в корзинке:", apples_left)