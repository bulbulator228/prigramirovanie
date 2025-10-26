def threat(fig, a, b, c, d):
    if fig == 'rook':
        return rook_threatens(a, b, c, d)
    elif fig == 'bishop':
        return bishop_threatens(a, b, c, d)
    elif fig == 'queen':
        return queen_threatens(a, b, c, d)
    elif fig == 'knight':
        return knight_threatens(a, b, c, d)
    elif fig == 'king':
        return king_moves(a, b, c, d)
    else:
        return False
def can_white_move_without_threat(w_fig, w_a, w_b, b_fig, b_a, b_b, e, f):
    b_threat = threat(b_fig, b_a, b_b, e, f)
    return not b_threat
w_fig = 'rook'
w_a, w_b = 1, 1
b_fig = 'queen'
b_a, b_b = 8, 8
e, f = 1, 8
print("Белая фигура может пойти без угрозы:", can_white_move_without_threat(w_fig, w_a, w_b, b_fig, b_a, b_b, e, f))
