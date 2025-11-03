def strange_husband(N):
    # Расчет расстояния после N-го этапа
    distance = 1
    total_path = 0
    direction = 1

    for k in range(1, N + 1):
        step = 1 / k
        total_path += step
        distance += direction * step
        # Меняем направление
        direction *= -1

    return distance, total_path

distance, total_path = strange_husband(100)
print(f"Расстояние от дома после 100-го этапа: {distance}")
print(f"Общий пройденный путь: {total_path}")