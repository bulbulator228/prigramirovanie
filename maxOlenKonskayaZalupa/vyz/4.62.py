a, b = map(float, input("Введите a и b: ").split())
c, d = map(float, input("Введите c и d: ").split())
if (a <= c and b <= d) or (b <= c and a <= d):
    print("Прямоугольник может уместиться")
else:
    print("Прямоугольник не уместится")
