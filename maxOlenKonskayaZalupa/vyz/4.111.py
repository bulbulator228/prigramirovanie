a = int(input('введите число a:'))
b = int(input('введите число b:'))
c = int(input('введите число c:'))
d = int(input('введите число d:'))
def count_even(a, b, c, d):
    return sum(1 for x in [a, b, c, d] if x % 2 == 0)
print(count_even(a, b, c, d))