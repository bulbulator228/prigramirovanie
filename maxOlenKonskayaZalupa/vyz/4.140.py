def full_card_name():
    m = int(input("Введите номер масти (1-4): "))
    k = int(input("Введите номер достоинства карты (6-14): "))
    suits = {1: "пик", 2: "треф", 3: "бубен", 4: "червей"}
    ranks = {11: "валет", 12: "дама", 13: "король", 14: "туз"}
    if m not in suits:
        print("Неверный номер масти")
        return
    if k in ranks:
        rank_name = ranks[k]
    elif 6 <= k <= 10:
        rank_name = str(k)
    else:
        print("Неверный номер достоинства карты")
        return
    print(f"{rank_name.capitalize()} {suits[m]}")