text=[ch for ch in input().split("|") if ch!=' ']

matrix=[]
for row in text:
    row=row.split()
    matrix.append([ch for ch in row if ch!=' '])
result=[]
for line in range(len(text)-1,-1,-1):
    result.extend(matrix[line])
print(*result)