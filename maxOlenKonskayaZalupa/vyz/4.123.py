points = int(input("Введите количество очков: "))

if points == 3:
    result = "выигрыш"
elif points == 0:
    result = "проигрыш"
elif points == 1:
    result = "ничья"
else:
    result = "недопустимое значение очков"

print("Результат игры:", result)