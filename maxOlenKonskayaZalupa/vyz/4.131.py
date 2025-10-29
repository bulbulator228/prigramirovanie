a1 = float(input("Введите первую тройку (через пробел): ").split()[0])
a2 = float(input())
a3 = float(input())
b1 = float(input("Введите вторую тройку: ").split()[0])
b2 = float(input())
b3 = float(input())
def get_middle_num(x, y, z):
    nums = [x, y, z]
    nums_sorted = sorted(nums)
    return nums_sorted[1]
middle_a = get_middle_num(a1, a2, a3)
middle_b = get_middle_num(b1, b2, b3)
average = (middle_a + middle_b) / 2
print(f"Среднее арифметическое средних чисел: {average}")