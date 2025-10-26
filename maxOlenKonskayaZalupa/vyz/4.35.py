n = int(input("Введите четырёхзначное число: "))
a = int(input("Введите число a: "))
d = [int(x) for x in str(n)]
sumkwo = d[0] + d[1]
sumtwo = d[2] + d[3]
s = sum(d)
p = 1
for x in d:
    p *= x
print("а) Сумма первых двух равна сумме последних двух?", sumkwo == sumtwo)
print("б) Сумма цифр кратна 3?", s % 3 == 0)
print("в) Произведение цифр кратно 4?", p % 4 == 0)
print("г) Произведение цифр кратно a?", a != 0 and p % a == 0)