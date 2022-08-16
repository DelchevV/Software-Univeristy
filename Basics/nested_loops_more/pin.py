first_limit=int(input())
second_limit=int(input())
third_limit=int(input())
for f in range(1,first_limit+1):
    for s in range(1,second_limit+1):
        for t in range(1,third_limit+1):
            if f%2==0 and t%2==0 and (s!=1 and s!=4 and s!=6 and s!=8 and s!=9):
                print(f,s,t)