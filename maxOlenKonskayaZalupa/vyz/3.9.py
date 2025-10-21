n = int(input("Введите количество секунд с начала суток: "))
hours = n // 3600
minutes = (n % 3600) // 60
seconds = n % 60
print("Полных часов:", hours)
print("Полных минут в текущем часе:", minutes)
print("Полных секунд в текущей минуте:", seconds)