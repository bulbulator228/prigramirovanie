count = 0
for num in range(100, 501):
    if sum(int(d) for d in str(num)) == 15:
        count += 1
print(count)