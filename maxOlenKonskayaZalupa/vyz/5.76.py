a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
for num in range(a, b + 1):
    if num % c == 0:
        print(num)