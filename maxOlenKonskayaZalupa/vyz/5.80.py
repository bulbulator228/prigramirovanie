n = int(input("Введите n: "))
for num in range(10, 100):
    digits = [int(d) for d in str(num)]
    if num % n == 0 or n in digits:
        print(num)