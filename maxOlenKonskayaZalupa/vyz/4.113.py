a = int(input('введите число a:'))
b = int(input('введите число b:'))
c = int(input('введите число c:'))
d = int(input('введите число d:'))
def sum_gt_five(a, b, c, d):
    return (a if a > 5 else 0) + (b if b > 5 else 0) + (c if c > 5 else 0) + (d if d > 5 else 0)
print(sum_gt_five(a,b,c,d))