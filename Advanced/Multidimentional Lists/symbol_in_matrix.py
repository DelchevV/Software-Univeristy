rows=int(input())
matrix=[]
for row in range(rows):
    matrix.append([ch for ch in input()])
searched_ch=input()
found=False
for row in range(rows):
    for col in range(rows):
        if matrix[row][col]==searched_ch:
            print(f'({row}, {col})')
            found=True
            break
        if found:
            break
if not found:
    print(f'{searched_ch} does not occur in the matrix')

