a, b = map(int, input("Введите размеры стола a b (a > b): ").split())
c, d, e = map(int, input("Введите размеры кости domino c d e (c > d > e): ").split())
faces = [(c, d), (c, e), (d, e)]
max_count = 0
for width, height in faces:
    # Проверяем два варианта размещения по сторонам стола
    count1 = (a // width) * (b // height)
    count2 = (a // height) * (b // width)
    max_count = max(max_count, count1, count2)
print(f"Максимальное количество костей, помещающихся на столе: {max_count}")
