max_star=int(input())
for i in range(1,max_star+1):
    for r in range(i):
        print("*", end='')
    print()
for i in range(max_star -1, 0, -1):
    for r in range(i):
        print("*", end='')
    print()