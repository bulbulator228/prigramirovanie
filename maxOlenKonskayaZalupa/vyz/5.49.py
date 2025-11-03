# Вариант а) прирост суммы вклада за первые 10 месяцев
initial_deposit = 1000
monthly_increase_rate = 0.02
deposits = [initial_deposit]
print("Прирост за каждый месяц:")
for month in range(1, 11):
    previous_amount = deposits[-1]
    growth = previous_amount * monthly_increase_rate
    new_amount = previous_amount + growth
    deposits.append(new_amount)
    print(f"Месяц {month}: прирост = {growth:.2f} руб.")

# Вариант б) сумма вклада через 3, 4, ..., 12 месяцев
print("\nСумма вклада через указанные месяцы:")
for month in range(3, 13):
    amount = initial_deposit * ((1 + monthly_increase_rate) ** month)
    print(f"Через {month} месяцев: {amount:.2f} руб.")