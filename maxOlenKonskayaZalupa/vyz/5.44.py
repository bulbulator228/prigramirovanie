def fibonacci_n(n):
    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b
n = int(input("Введите n (≥3): "))
print(f"{n}-й член последовательности Фибоначчи: {fibonacci_n(n)}")

#б
def fibonacci_sequence(n):
    seq = [1, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq

n = int(input("Введите n (≥3): "))
sequence = fibonacci_sequence(n)
print("Первые n членов последовательности Фибоначчи:")
print(sequence)