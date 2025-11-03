# сумма 2^2 + 2^3 + ... + 2^10 без возведения в степень
total = 0
current_power = 4  # 2^2 = 4
for exponent in range(2, 11):
    sum_prev = current_power
    # умножаем на 2, чтобы получить следующую степень
    current_power = sum_prev + sum_prev  # эквивалентно 2 * sum_prev
    total += current_power
print(f"Сумма: {total}")
total = 0
current = 4  # 2^2
for _ in range(2, 11):
    total += current
    # умножение на 2 для следующей степени
    current = current * 2
print(f"Сумма: {total}")