#a
for num in range(10, 100):
    digits = [int(d) for d in str(num)]
    sum_squares = sum(d**2 for d in digits)
    if sum_squares % 13 == 0:
        print(num)
#b
for num in range(10, 100):
    digits = [int(d) for d in str(num)]
    s = sum(digits)
    if s + s**2 == num:
        print(num)