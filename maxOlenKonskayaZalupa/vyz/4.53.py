num = input("Введите трёхзначное число: ")
print("Входят ли цифры 4 или 7:", '4' in num or '7' in num)
print("Входят ли цифры 3, 6 или 9:", any(d in num for d in ['3', '6', '9']))
