birth_year = int(input("Введите год рождения: "))
birth_month = int(input("Введите месяц рождения (1-12): "))
current_year = int(input("Введите текущий год: "))
current_month = int(input("Введите текущий месяц (1-12): "))
age = current_year - birth_year
if current_month < birth_month:
    age -= 1
print(f"Возраст: {age} лет")
