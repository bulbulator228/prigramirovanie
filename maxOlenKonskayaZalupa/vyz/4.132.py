x = float(input("Введите X: "))
y = float(input("Введите Y: "))
if x > 0 and y > 0:
    print("Точка в первой четверти")
elif x < 0 and y > 0:
    print("Точка во второй четверти")
elif x < 0 and y < 0:
    print("Точка в третьей четверти")
elif x > 0 and y < 0:
    print("Точка в четвертой четверти")