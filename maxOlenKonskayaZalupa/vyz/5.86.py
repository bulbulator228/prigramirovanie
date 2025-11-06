total = sum(i for i in range(31, 100) if i % 3 == 0 and str(i)[-1] in ['2', '4', '8'])
print(total)