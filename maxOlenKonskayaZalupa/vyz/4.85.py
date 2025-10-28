def age_in_years_months(n):
    years = n // 12
    months = n % 12
    def years_word(y):
        if 11 <= (y % 100) <= 14:
            return "лет"
        last = y % 10
        if last == 1:
            return "год"
        elif 2 <= last <= 4:
            return "года"
        else:
            return "лет"
    def months_word(m):
        if 11 <= (m % 100) <= 14:
            return "месяцев"
        last = m % 10
        if last == 1:
            return "месяц"
        elif 2 <= last <= 4:
            return "месяца"
        else:
            return "месяцев"
    if months == 0:
        return f"{years} {years_word(years)} ровно"
    else:
        return f"{years} {years_word(years)} {months} {months_word(months)}"
print(age_in_years_months(250))
print(age_in_years_months(624))
print(age_in_years_months(552))
