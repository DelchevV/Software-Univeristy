def check_right():
    for direction in directions:
        r, c = king_pos
        while True:
            r += direction[0]
            c += direction[1]
            if 0 <= r < size and 0 <= c < size:
                if board[r][c] == "Q":
                    queens_that_capture.append([r, c])
                    break
            else:
                break


size = 8
board = [input().split() for _ in range(size)]
directions = (
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1),
)

king_pos = []
queens_that_capture = []

for row in range(size):
    for col in range(size):
        if board[row][col] == "K":
            king_pos.append(row)
            king_pos.append(col)

row, col = king_pos
check_right()

if queens_that_capture:
    for queen in queens_that_capture:
        print(queen)
else:
    print('The king is safe!')
