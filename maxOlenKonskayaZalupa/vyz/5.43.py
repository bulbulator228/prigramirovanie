def generate_sequence_a(n):
    a = [1]
    for k in range(1, n + 1):
        a_k = k * a[-1] + 1 / k
        a.append(a_k)
    return a

n = int(input("Введите n: "))
sequence = generate_sequence_a(n)
print("Полученная последовательность:")
for idx, val in enumerate(sequence):
    print(f"a{idx} = {val}")