def f(x):
    if x <= 0:
        return 0
    if 0 <= x <=1:
        return x
    if x ==  (float('-inf'), 0) or x == (float('inf'), 1):
        return x**2
a_value = float(input("Введите a: "))
print("z(a) =", f(a_value))