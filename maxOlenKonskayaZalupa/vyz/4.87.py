g1, m1, d1 = map(int, input("Первый: год, месяц, день: ").split())
g2, m2, d2 = map(int, input("Второй: год, месяц, день: ").split())

if (g1, m1, d1) < (g2, m2, d2):
    print("Первый старше")
elif (g1, m1, d1) > (g2, m2, d2):
    print("Второй старше")
else:
    print("Они одного возраста")