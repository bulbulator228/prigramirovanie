age_mitya = int(input("Возраст Мити: "))
age_vasya = int(input("Возраст Васи: "))

if age_mitya > age_vasya:
    print("Митя старше Васи")
elif age_mitya < age_vasya:
    print("Вася старше Мити")
else:
    print("Митя и Вася одного возраста")