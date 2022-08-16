number=input()
for n1 in range(1,int(number[2])+1):
    for n2 in range(1,int(number[1])+1):
        for n3 in range(1,int(number[0])+1):
            print(f"{n1} * {n2} * {n3} = {n1*n2*n3};")
