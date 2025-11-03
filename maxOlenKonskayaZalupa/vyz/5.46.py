def sequence_fraction_k(k):
    if k == 1:
        numerator, denominator = 1, 1
    else:
        # Используем формулы для числителя и знаменателя
        # Простая реализация: строим последовательно
        numerators = [1, 2]
        denominators = [1, 1]
        for i in range(2, k):
            numerators.append(numerators[-1] + numerators[-2])
            denominators.append(denominators[-1] + denominators[-2])
        numerator = numerators[k - 1]
        denominator = denominators[k - 1]
    return numerator / denominator

k = int(input("Введите k: "))
print(f"{k}-й член последовательности: {sequence_fraction_k(k)}")


#б
def sequence_fractions(n):
    numerators = [1, 2]
    denominators = [1, 1]
    sequence = [(1/1), (2/1)]
    for i in range(2, n):
        numerators.append(numerators[-1] + numerators[-2])
        denominators.append(denominators[-1] + denominators[-2])
        sequence.append(numerators[-1] / denominators[-1])
    return sequence

n = int(input("Введите n: "))
sequence = sequence_fractions(n)
print("Первые n членов:")
for idx, val in enumerate(sequence, start=1):
    print(f"Член {idx}: {val}")