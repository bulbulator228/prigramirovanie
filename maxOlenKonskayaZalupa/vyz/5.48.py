def amoeba_cells(hours):
    # исходное количество клеток
    cells = 1
    results = []
    for t in range(3, hours + 1, 3):
        cells *= 2
        results.append((t, cells))
    return results

hours = [3 * i for i in range(1, 9)]  # 3, 6, 9, ..., 24
results = amoeba_cells(24)
for t, count in results:
    print(f"Через {t} часов: {count} клеток")