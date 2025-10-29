def f(y):
    if y > 2:
        return 2
    if 0< y <=2 :
        return 0
    if y == (float('-inf'), 0):
        return -3 *y
y_value = float(input("Введите y: "))
print("y(x) =", f(y_value))