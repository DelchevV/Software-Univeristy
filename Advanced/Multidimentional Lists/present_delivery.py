presents = int(input())
size = int(input())
matrix = [[ch for ch in input().split()] for _ in range(size)]
start_pos = []
nice_kids = 0

for row in range(size):

    for col in range(size):
        if matrix[row][col] == "S":
            start_pos = [row, col]
        if matrix[row][col] == "V":
            nice_kids += 1
copy_of_nice_kids=nice_kids
while True:

    p1, p2 = start_pos

    command = input()
    if command == "Christmas morning":
        break
    matrix[p1][p2] = "-"
    if command == "up":
        if 0 <= p1 - 1 < size and 0 <= p2 < size:
            p1 -= 1
    elif command == "down":
        if 0 <= p1 + 1 < size and 0 <= p2 < size:
            p1 += 1
    elif command == "left":
        if 0 <= p1  < size and 0 <= p2-1 < size:
            p2 -= 1
    elif command == "right":
        if 0 <= p1  < size and 0 <= p2+1 < size:
            p2 += 1

    if matrix[p1][p2] == "V":
        matrix[p1][p2] = "-"
        presents -= 1
        nice_kids -= 1
    elif matrix[p1][p2] == 'C':
        if (matrix[p1-1][p2] == "V" or matrix[p1-1][p2]=="X") and presents>0:
            presents-=1

            if matrix[p1][p2] == "V":
                nice_kids-=1
            matrix[p1 - 1][p2] = '-'

        if matrix[p1+1][p2] == "V" or matrix[p1+1][p2]=="X" and presents>0:
            presents-=1

            if matrix[p1+1][p2] == "V":
                nice_kids-=1
            matrix[p1 + 1][p2] = '-'

        if matrix[p1][p2-1] == "V" or matrix[p1][p2-1]=="X" and presents>0:
            presents-=1

            if matrix[p1][p2-1] == "V":
                nice_kids-=1
            matrix[p1][p2 - 1] = "-"

        if matrix[p1][p2+1] == "V" or matrix[p1][p2+1]=="X" and presents>0:
            presents-=1

            if matrix[p1][p2+1] == "V":
                nice_kids-=1
            matrix[p1][p2 + 1] = '-'

    elif matrix[p1][p2] == "X":
        matrix[p1][p2] = "-"

    start_pos=[p1,p2]
    matrix[p1][p2]="S"
    if presents<=0:
        break
if presents<=0 and nice_kids!=0:
    print("Santa ran out of presents!")
for r in matrix:
    print(*r)
if nice_kids==0:
    print(f"Good job, Santa! {copy_of_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids} nice kid/s.")
