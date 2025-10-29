a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))
numbers = [a, b, c]
numbers_sorted = sorted(numbers)
product_two_smallest = numbers_sorted[0] * numbers_sorted[1]
print(f"Произведение двух наименьших чисел: {product_two_smallest}")