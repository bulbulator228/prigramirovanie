a, b = map(float, input("Введите два числа: ").split())

# а) полусумма абсолютных
abs_a = a if a >= 0 else -a
abs_b = b if b >= 0 else -b
half_sum = (abs_a + abs_b) / 2

# б) корень из произведения абсолютных
import math
product_sqrt = math.sqrt(abs_a * abs_b)

print("Полусумма абсолютных:", half_sum)
print("Квадратный корень из произведения:", product_sqrt)