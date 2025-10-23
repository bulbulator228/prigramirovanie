k = int(input("Введите k (1-180): "))
pair_index = (k + 1) // 2
number = 10 + pair_index - 1
if k % 2 == 1:
    digit = number // 10
else:
    digit = number % 10
print(f"Номер пары: {pair_index}")
print(f"Двузначное число: {number}")
print(f"k-я цифра ({'нечетное' if k%2==1 else 'четное'} k): {digit}")
