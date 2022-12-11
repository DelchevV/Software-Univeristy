def print_row(sizes, count_starts):
    for row in range(sizes-count_starts):
        print(" ",end="")
    for row in range(1,count_starts):
        print("* ",end="")
    print("*")


size = int(input())

for n in range(1, size + 1):
    print_row(size,n)

for r in range(size, 0, -1):
    print_row(size,r)
