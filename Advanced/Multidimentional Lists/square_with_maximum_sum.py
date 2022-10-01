rows, cols = map(int, input().split(', '))
matrix = []
for row in range(rows):
    matrix.append([int(i) for i in input().split(', ')])

best_square=list()
total_sum = 0
for row in range(rows):
    for col in range(cols):
        first = matrix[row][col]
        if col + 1 < cols:
            second = matrix[row][col + 1]
        else:
            break
        if row + 1 < rows:
            third = matrix[row + 1][col]
        else:
            break
        if row + 1 < rows and col + 1 <= cols:
            forth = matrix[row + 1][col + 1]
        else:
            break
        current_sum = first + second + third + forth
        if current_sum > total_sum:
            total_sum = current_sum
            best_square=[[first,second],[third,forth]]
for row in best_square:
    print(' '.join(map(str,row)))
print(total_sum)
