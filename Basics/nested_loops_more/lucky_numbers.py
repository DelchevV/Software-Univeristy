number=int(input())
for i1 in range(1,9+1):
    for i2 in range(1,9+1):
        for i3 in range(1,9+1):
            for i4 in range(1,9+1):
                if i1+i2==i3+i4:
                    if number%(i1+i2)==0:
                        print(f"{i1}{i2}{i3}{i4}",end=" ")

