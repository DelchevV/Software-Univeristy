lines=int(input())
odd_set=set()
even_set=set()
for line in range(1,lines+1):
    name=input()
    sum_of_ch=0
    for ch in name:
        sum_of_ch+=ord(ch)
    sum_of_ch=int(sum_of_ch/line)
    if sum_of_ch%2==0:
        even_set.add(sum_of_ch)
    else:
        odd_set.add(sum_of_ch)

if sum(odd_set)==sum(even_set):
    result=odd_set.union(even_set)
    print(", ".join(map(str,result )))
elif sum(odd_set)>sum(even_set):
    result=odd_set.difference(even_set)
    print(", ".join(map(str, result)))
elif sum(odd_set)<sum(even_set):
    result=odd_set.symmetric_difference(even_set)
    print(", ".join(map(str, result)))