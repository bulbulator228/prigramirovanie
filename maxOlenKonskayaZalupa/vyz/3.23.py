num = int(input("Введите трёхзначное число: "))
c = num % 10
ab = num // 10
new_num = c * 100 + ab
print("Новое число:", new_num)