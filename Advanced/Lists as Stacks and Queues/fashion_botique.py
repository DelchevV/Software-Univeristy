clothes=[int(i) for i in input().split()]

rack_cap=int(input())
count_of_racks=1
sum_of_clothes=0
while clothes:
    current_clothes=clothes.pop()
    if sum_of_clothes+current_clothes<=rack_cap:
        sum_of_clothes+=current_clothes
    else:
        count_of_racks+=1
        sum_of_clothes=current_clothes
print(count_of_racks)



