n = int(input("Введите натуральное число (n > 9): "))
units = n % 10
tens = (n // 10) % 10
print("а) Число единиц:", units)
print("б) Число десятков:", tens)