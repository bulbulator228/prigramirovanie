def z(a):
    if a < 0:
        return -1
    if a > 0:
        return 1
    if a == 0:
        return 0
a_value = float(input("Введите a: "))
print("z(a) =", z(a_value))