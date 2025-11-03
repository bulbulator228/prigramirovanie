a = float(input("Введите число a: "))
n = int(input("Введите натуральное число n: "))
# вычисляем последовательность a1, a2, ..., an
sequence = []
for i in range(1, n + 1):
    a_i = a * i
    sequence.append(a_i)
    print(f"a_{i} = {a_i}")