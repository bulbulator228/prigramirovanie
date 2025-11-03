sum_result = 0
for i in range(1, 11):
    term = (i * 10) ** 2
    if i % 2 == 1:
        sum_result += term  # нечётные: +
    else:
        sum_result -= term  # чётные: -
print(f"Итоговая сумма: {sum_result}")