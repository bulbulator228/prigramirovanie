kurs = float(input("Введите курс рубля к доллару: "))
for dollar in range(1, 21):
    rublis = dollar * kurs
    print(f"{dollar}$ = {rublis:.2f} руб.")