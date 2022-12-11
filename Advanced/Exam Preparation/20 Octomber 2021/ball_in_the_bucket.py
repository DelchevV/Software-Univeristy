rows = 6
matrix = [input().split() for _ in range(rows)]

points = 0

for _ in range(3):
    row, col = map(int, input().strip('(').strip(')').split(', '))
    if 0 <= row < rows and 0 <= col < rows:
        if matrix[row][col] == "B":

            for r in range(rows):
                if matrix[r][col] != "B":
                    points += int(matrix[r][col])
        matrix[row][col] = "."

if points < 100:
    print(f'Sorry! You need {100 - points} points more to win a prize.')
else:
    gift=''
    if 100 <= points <= 199:
        gift = "Football"
    elif 200 <= points <= 299:
        gift = "Teddy Bear"
    elif points >= 300:
        gift = "Lego Construction Set"
    print(f"Good job! You scored {points} points, and you've won {gift}.")
