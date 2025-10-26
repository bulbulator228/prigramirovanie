def is_triangle_exists(a, b, c):
    pass
def is_right_triangle(a, b, c):
    if not is_triangle_exists(a, b, c):
        return False
    sides = sorted([a, b, c])
    return abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < 1e-9
