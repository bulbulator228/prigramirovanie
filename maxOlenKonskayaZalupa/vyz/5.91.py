num = int(input("Введите число: "))
divisors = [d for d in range(1, num + 1) if num % d == 0]
print("Делители:", divisors)
print("Сумма делителей:", sum(divisors))
even_divs = [d for d in divisors if d % 2 == 0]
print("Сумма четных делителей:", sum(even_divs))
print("Количество делителей:", len(divisors))
print("Количество нечетных делителей:", len(divisors) - len(even_divs))
print("Четных делителей:", len(even_divs))
d = int(input("Введите значение d: "))
large_divs = [d for d in divisors if d > d]
print(f"Кол-во делителей, больших {d}:", len(large_divs))