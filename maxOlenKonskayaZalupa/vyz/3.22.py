num = int(input("Введите трёхзначное число: "))
a = num // 100
bc = num % 100
new_num = bc * 10 + a
print("Новое число:", new_num)