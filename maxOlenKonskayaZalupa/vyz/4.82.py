def age_phrase(n):
    # n - возраст в годах
    if 11 <= (n % 100) <= 14:
        suffix = "лет"
    else:
        last = n % 10
        if last == 1:
            suffix = "год"
        elif 2 <= last <= 4:
            suffix = "года"
        else:
            suffix = "лет"
    return f"мне {n} {suffix}"

print(age_phrase(21))
print(age_phrase(32))
print(age_phrase(15))
