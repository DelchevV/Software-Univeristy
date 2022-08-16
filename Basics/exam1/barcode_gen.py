start=input()
end=input()
for n1 in range(start[0],end[0]):
    for n2 in range(start[1],end[1]):
        for n3 in range(start[2],end[2]):
            for n4 in range(start[3],end[3]):
                if n1%2!=0 and n2%2!=0 and n3%2!=0 and n4%2!=0:
                    print(f"{n1}{n2}{n3}{n4}", end="")