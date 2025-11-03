def fibonacci_range(start, end):
    seq = [1, 1]
    for _ in range(2, end):
        seq.append(seq[-1] + seq[-2])
    return seq[start-1:end]

result = fibonacci_range(3, 10)
print("Члены с 3-го по 10-й:")
for idx, val in enumerate(result, start=3):
    print(f"a{idx} = {val}")