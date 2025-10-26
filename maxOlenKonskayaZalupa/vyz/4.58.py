a, b, c = map(float, input("Введите три числа a, b, c: ").split())
pair = (a == b) or (b == c) or (a == c)
print("Есть равные числа:", pair)
