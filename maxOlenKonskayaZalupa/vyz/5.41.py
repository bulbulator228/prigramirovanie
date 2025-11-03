def sum_and_product_last_n_digits(number, n):
    sum_digits = 0
    product_digits = 1
    for _ in range(n):
        digit = number % 10
        sum_digits += digit
        product_digits *= digit
        number //= 10
    return sum_digits, product_digits

# Пример использования:
num = int(input("Введите число: "))
n = int(input("Введите количество последних цифр n: "))
sum_digits, product_digits = sum_and_product_last_n_digits(num, n)
print(f"Сумма последних {n} цифр: {sum_digits}")
print(f"Произведение последних {n} цифр: {product_digits}")