def price_in_rubles(n):
    rub = n // 100
    kop = n % 10
    def rubles_word(r):
        if 11 <= (r % 100) <= 14:
            return "рублей"
        last = r % 10
        if last == 1:
            return "рубль"
        elif 2 <= last <= 4:
            return "рубля"
        else:
            return "рублей"

    def kopecks_word(k):
        if 11 <= (k % 100) <= 14:
            return "копеек"
        last = k % 10
        if last == 1:
            return "копейка"
        elif 2 <= last <= 4:
            return "копейки"
        else:
            return "копеек"

    if kop == 0:
        return f"{rub} {rubles_word(rub)} ровно"
    else:
        return f"{rub} {rubles_word(rub)} {kop} {kopecks_word(kop)}"

print(price_in_rubles(321))
print(price_in_rubles(1505))
print(price_in_rubles(100))
