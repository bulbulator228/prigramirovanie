a = int(input('введите число a:'))
b = int(input('введите число b:'))
c = int(input('введите число c:'))
def sum_positive(a, b, c):
    return sum(x for x in [a, b, c] if x > 0)
print(sum_positive(a, b, c))