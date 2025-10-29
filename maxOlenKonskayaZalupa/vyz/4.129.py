a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))
numbers = [a, b, c]
numbers_sorted = sorted(numbers, reverse=True)
sum_two_largest = numbers_sorted[0] + numbers_sorted[1]
print(f"Сумма двух наибольших чисел: {sum_two_largest}")