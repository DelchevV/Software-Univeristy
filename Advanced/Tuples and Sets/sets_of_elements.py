n,m=map(int,input().split())
set_n=set()
set_m=set()
for i in range(n):
    set_n.add(int(input()))
for y in range(m):
    set_m.add(int(input()))
result=set_n&set_m
for res in result:
    print(res)

