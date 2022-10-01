rows = int(input())
matrix = []
for row in range(rows):
    matrix.append([int(i) for i in input().split()])
diag_sum = 0
for row in range(rows):
    diag_sum += matrix[row][row]
print(diag_sum)
