rows = 8
matrix = [input().split() for row in range(8)]
white_cords = []
black_cords = []

diagonals_white = (
    (-1, 1),
    (-1, -1)
)

diagonals_black = (
    (1, 1),
    (1, -1)
)

is_captured = False

for row in range(rows):
    for col in range(rows):
        if matrix[row][col] == "w":
            white_cords = [row, col]
        elif matrix[row][col] == "b":
            black_cords = [row, col]


def check_pos(winner_cords):
    r, c = winner_cords
    if r== 0: r='8'
    elif r==1: r='7'
    elif r==2: r='6'
    elif r==3: r='5'
    elif r==4: r='4'
    elif r==5: r='3'
    elif r==6: r='2'
    elif r==7: r='1'

    if c==0: c='a'
    elif c==1: c='b'
    elif c==2: c='c'
    elif c==3: c='d'
    elif c==4: c='e'
    elif c==5: c='f'
    elif c==6: c='g'
    elif c==7: c='h'

    return c+r


while True:
    white_r, white_c = white_cords
    black_r, black_c = black_cords

    for diag in diagonals_white:
        r, c = diag
        if white_r + r == black_r and white_c + c == black_c:
            white_cords=[white_r+r,white_c+c]
            square=check_pos(white_cords)
            print(f"Game over! White win, capture on {square}.")
            is_captured = True
            break

    if is_captured:
        break

    if white_r - 1 == 0:
        white_cords=[white_r-1,white_c]
        square=check_pos(white_cords)
        print(f"Game over! White pawn is promoted to a queen at {square}.")
        break
    else:
        white_r -= 1

    white_cords = [white_r, white_c]

    for diag in diagonals_black:
        r, c = diag
        if black_r + r == white_r and black_c + c == white_c:
            black_cords=[black_r+r, black_c+c]
            square = check_pos(black_cords)
            print(f"Game over! Black win, capture on {square}.")
            is_captured = True

    if is_captured:
        break

    if black_r + 1 == rows - 1:
        black_cords=[black_r+1,black_c]
        square=check_pos(black_cords)
        print(f"Game over! Black pawn is promoted to a queen at {square}.")
        break
    else:
        black_r += 1
    black_cords = [black_r, black_c]

