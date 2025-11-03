def get_vn(n):
    v = [0, 0, 1.5]
    if n <= 3:
        return v[n-1]
    for i in range(3, n):
        v_new = v[i - 1] + v[i - 3]
        v.append(v_new)
    return v[n-1]

n = int(input("Введите n (≥4): "))
print(f"v{n} = {get_vn(n)}")