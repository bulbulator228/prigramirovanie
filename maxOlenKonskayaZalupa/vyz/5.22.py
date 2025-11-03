price_per_kg_conf = float(input("Введите стоимость 1 кг конфет: "))
print("\nТовар       Вес (г)    Стоимость")
for weight in range(100, 2001, 100):
    cost = (weight / 1000) * price_per_kg_conf
    print(f"Конфеты    {weight}      {cost:.2f}")