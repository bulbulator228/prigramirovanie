cost_candy = float(input("Цена 1 кг конфет: "))
cost_cookies = float(input("Цена 1 кг печенья: "))
cost_apples = float(input("Цена 1 кг яблок: "))

x = float(input("Килограммы конфет: "))
y = float(input("Килограммы печенья: "))
z = float(input("Килограммы яблок: "))

total = x * cost_candy + y * cost_cookies + z * cost_apples
print("Общая стоимость покупки:", total)
