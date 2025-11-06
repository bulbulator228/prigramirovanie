#a
for num in range(100, 1000):
    sq = num * num
    if str(sq)[-3:] == str(num):
        print(num)
#b
for num in range(100, 1000):
    digits_sum = sum(int(d) for d in str(num))
    if num % 7 == 0 and digits_sum % 7 == 0:
        print(num)
