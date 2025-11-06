s = int(input("Введите s (1-27): "))
count = 0
for num in range(100, 1000):
    if sum(int(d) for d in str(num)) == s:
        count += 1
print(count)