# а) все целые числа от 20 до 35
for i in range(20, 36):
    print(i)

# б) квадраты чисел от a до 50 (ввод)
a = int(input("Введите a ( ≤ 50): "))
for i in range(a, 51):
    print(i*i)

# в) кубы чисел от 10 до b (ввод)
b = int(input("Введите b ( ≥ 10): "))
for i in range(10, b+1):
    print(i**3)

# г) числа от a до b (ввод)
a = int(input("Введите a: "))
b = int(input("Введите b: "))
for i in range(a, b+1):
    print(i)