from itertools import permutations
num = input("Введите трёхзначное число с различными цифрами: ")
digits = list(num)
perms = set()
for p in permutations(digits):
    perms.add(''.join(p))
print("Все перестановки:", ', '.join(sorted(perms)))