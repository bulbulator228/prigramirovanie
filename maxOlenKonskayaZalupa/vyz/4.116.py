def y(x):
    if x < -1:
        return -1
    if x > -1:
        return x
    if x == -1:
        return 1
x_value = float(input("Введите x: "))
print("y(x) =", y(x_value))