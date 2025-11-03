# а) урожайность за 2-й, 3-й, ..., 8-й год
initial_yield = 20
area_growth = 0.05
yield_growth = 0.02
yields = [initial_yield]
for year in range(2, 9):
    new_yield = yields[-1] * (1 + yield_growth)
    yields.append(new_yield)
print("Урожайность по годам:")
for i, y in enumerate(yields, start=1):
    print(f"Год {i}: {y:.2f} ц/га")
    
# б) площадь участка в 4, 5, ..., 7 год
initial_area = 100
area_list = [initial_area]
for year in range(2, 8):
    new_area = area_list[-1] * (1 + area_growth)
    area_list.append(new_area)
print("\nПлощадь участка по годам:")
for i, area in enumerate(area_list[3:], start=4):
    print(f"Год {i}: {area:.2f} га")

# в) урожай за первые 6 лет
total_harvest = 0
area_current = initial_area
yield_current = initial_yield
for year in range(6):
    total_harvest += area_current * yield_current
    area_current *= (1 + area_growth)
    yield_current *= (1 + yield_growth)
print(f"\nОбщий урожай за 6 лет: {total_harvest:.2f} ц")