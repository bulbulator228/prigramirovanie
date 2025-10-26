def rook_threat(a, b, c, d):
    return a == c or b == d
def bishop_threat(a, b, c, d):
    return abs(a - c) == abs(b - d)
def king_move(a, b, c, d):
    return max(abs(a - c), abs(b - d)) == 1
def queen_threat(a, b, c, d):
    return rook_threat(a, b, c, d) or bishop_threat(a, b, c, d)
def white_pawn_move(a, b, c, d):
    normal = (c == a) and (d == b + 1)
    take = (abs(c - a) == 1) and (d == b + 1)
    return normal, take
def black_pawn_move(a, b, c, d):
    normal = (c == a) and (d == b - 1)
    take = (abs(c - a) == 1) and (d == b - 1)
    return normal, take
def knight_threat(a, b, c, d):
    dx = abs(a - c)
    dy = abs(b - d)
    return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)
a = int(input("Введите номер вертикали фигуры a (1-8): "))
b = int(input("Введите номер горизонтали фигуры b (1-8): "))
c = int(input("Введите номер вертикали цели c (1-8): "))
d = int(input("Введите номер горизонтали цели d (1-8): "))
print("\nЛадья угрожает полю:", "Да" if rook_threat(a, b, c, d) else "Нет")
print("Слон угрожает полю:", "Да" if bishop_threat(a, b, c, d) else "Нет")
print("Король может ходить на поле:", "Да" if king_move(a, b, c, d) else "Нет")
print("Ферзь угрожает полю:", "Да" if queen_threat(a, b, c, d) else "Нет")
wp_n, wp_t = white_pawn_move(a, b, c, d)
print("Белая пешка может сделать обычный ход:", "Да" if wp_n else "Нет")
print("Белая пешка может побить фигуру:", "Да" if wp_t else "Нет")
bp_n, bp_t = black_pawn_move(a, b, c, d)
print("Чёрная пешка может сделать обычный ход:", "Да" if bp_n else "Нет")
print("Чёрная пешка может побить фигуру:", "Да" if bp_t else "Нет")
print("Конь угрожает полю:", "Да" if knight_threat(a, b, c, d) else "Нет")

