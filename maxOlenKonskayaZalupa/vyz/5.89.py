count = 0
for num in range(100, 1000):
    digits_sum = sum(int(d) for d in str(num))
    if num % 7 == 0 and digits_sum % 7 == 0:
        count += 1
print(count)