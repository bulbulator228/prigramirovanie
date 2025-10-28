def mushrooms_phrase(k):
    if 11 <= (k % 100) <= 14:
        suffix = "грибов"
    else:
        last = k % 10
        if last == 1:
            suffix = "гриб"
        elif 2 <= last <= 4:
            suffix = "гриба"
        else:
            suffix = "грибов"
    return f"мы нашли {k} {suffix} в лесу"
print(mushrooms_phrase(1))
print(mushrooms_phrase(3))
print(mushrooms_phrase(12))
