print("Фунты\tКг")
for pounds in range(1, 11):
    kg = pounds * 453 / 1000
    print(f"{pounds}\t{kg:.2f}")