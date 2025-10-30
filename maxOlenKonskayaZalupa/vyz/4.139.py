def card_rank():
    k = int(input("Введите номер карты (6-14 или 17 для туза): "))
    ranks = {11: "валет", 12: "дама", 13: "король", 17: "туз"}
    if k in ranks:
        print(ranks[k])
    elif 6 <= k <= 14:
        print(str(k))
    else:
        print("Неверный номер карты")
