rows,cols=list(map(int,input().split()))
matrix=[]
for row in range(97,97+rows):
    current_row=[]
    for col in range(97,97+cols):
        symbol=chr(row)+chr(col+row-97)+chr(row)
        current_row.append(symbol)
    matrix.append(current_row)
for row in matrix:
    print(*row)