rows = int(input())
matrix = [[ch for ch in input()] for _ in range(rows)]
positions = (
    (-2, -1), (-2, 1),
    (-1, -2), (-1, 2),
    (1, -2), (1, 2),
    (2, -1), (2, 1)
)
removed_knights = 0
while True:
    max_attack = 0
    knight_with_most_kills = []
    for row in range(rows):
        for col in range(rows):

            if matrix[row][col] == 'K':
                attacks = 0

                for pos in positions:
                    p1=row+pos[0]
                    p2=col+pos[1]
                    if 0 <= p1 < rows and 0 <= p2 < rows:
                        if matrix[p1][p2] == "K":
                            attacks += 1

                if attacks > max_attack:
                    max_attack = attacks
                    knight_with_most_kills = [row, col]

    if knight_with_most_kills:
        matrix[knight_with_most_kills[0]][knight_with_most_kills[1]] = '0'
        removed_knights += 1
    else:
        break
print(removed_knights)
