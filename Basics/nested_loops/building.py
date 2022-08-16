floors=int(input())
rooms=int(input())

for f in range(floors,0,-1):
    print()
    if f==floors:
        for r in range(rooms):
            print(f"L{f}{r} ", end="")
    elif f%2==0:
        for r in range(rooms):
            print(f"O{f}{r} ", end="")

    elif f%2!=0:
        for r in range(rooms):
            print(f"A{f}{r} ", end="")


