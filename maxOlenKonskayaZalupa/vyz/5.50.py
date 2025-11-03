# а) пробег лыжника за второй, третий, ..., десятый день
initial_distance = 10
growth_rate = 0.10
distances = [initial_distance]
for day in range(2, 11):
    previous_distance = distances[-1]
    current_distance = previous_distance * (1 + growth_rate)
    distances.append(current_distance)
    print(f"День {day}: {current_distance:.2f} км")

# б) суммарный путь за первые 7 дней
total_distance = sum(distances[:7])
print(f"\nОбщий пробег за первые 7 дней: {total_distance:.2f} км")