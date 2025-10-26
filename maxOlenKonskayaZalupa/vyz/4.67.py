num = input("Введите шестизначное число: ")
if len(num) == 6 and num.isdigit():
    first_sum = sum(int(d) for d in num[:3])
    last_sum = sum(int(d) for d in num[3:])
    if first_sum == last_sum:
        print("Число счастливое")
    else:
        print("Число не счастливое")
else:
    print("Ввод не корректен")
