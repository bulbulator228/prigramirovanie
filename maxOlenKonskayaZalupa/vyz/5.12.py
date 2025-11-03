import math
p0 = 1.29
z = 1.25e-4
print("Высота м\tПлотность кг/м^3")
for h in range(0, 1100, 100):
    p = p0 * math.exp(-z * h)
    print(f"{h}\t\t{p:.3f}")
