n = int(input("Введите число: "))
if n > 1:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("Число не простое")
            break
    else:
        print("Число простое")
else:
    print("Число должно быть больше 1")