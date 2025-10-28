a, b, c, d, n, m = map(int, input("Введите a, b, c, d, n, m: ").split())

departure_start = a * 60 + b
departure_end = c * 60 + d
arrival = n * 60 + m

if departure_start <= arrival <= departure_end:
    print("Поезд стоит на платформе")
else:
    print("Поезд уехал")