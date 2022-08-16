count_of_groups=int(input())
musala=0
monblan=0
kilimandgaro=0
k2=0
everest=0
people=0
for i in range(count_of_groups):
    people_in_group=int(input())
    if people_in_group<=5:
        musala+=people_in_group
    elif people_in_group<=12:
        monblan+=people_in_group
    elif people_in_group<=25:
        kilimandgaro+=people_in_group
    elif people_in_group<=40:
        k2+=people_in_group
    elif people_in_group>=41:
        everest+=people_in_group
    people+=people_in_group
print(f"{musala/people*100:.2f}%")
print(f"{monblan/people*100:.2f}%")
print(f"{kilimandgaro/people*100:.2f}%")
print(f"{k2/people*100:.2f}%")
print(f"{everest/people*100:.2f}%")