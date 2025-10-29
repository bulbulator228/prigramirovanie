a = int(input('введите число a:'))
b = int(input('введите число b:'))
c = int(input('введите число c:'))
d = int(input('введите число d:'))
e = int(input('введите число e:'))
f = int(input('введите число f:'))
def sum_positive_six(a, b, c, d, e, f):
    return sum(x for x in [a, b, c, d, e, f] if x > 0)
print(sum_positive_six(a, b, c, d, e, f))