k = int(input("Введите k (1-150): "))
num_index = (k - 1) // 3
num = 101 + num_index
pos_in_num = (k - 1) % 3
digit = (num // (10 ** (2 - pos_in_num))) % 10
print(f"k-я цифра: {digit}")
