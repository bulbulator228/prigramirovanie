n = int(input("Введите натуральное число (n > 99): "))
tens = (n // 10) % 10
hundreds = (n // 100) % 10
print("а) Число десятков:", tens)
print("б) Число сотен:", hundreds)