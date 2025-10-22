n = int(input("Введите натуральное число (n > 999): "))
hundreds = (n // 100) % 10
thousands = (n // 1000) % 10
print("а) Число сотен:", hundreds)
print("б) Число тысяч:", thousands)