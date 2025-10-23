a = int(input("Введите a: "))
b = int(input("Введите b: "))
ans = 1 if (a % b == 0 or b % a == 0) else 0
print(ans)
