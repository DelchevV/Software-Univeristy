trunk_capacity=float(input())
taken_space=0
suitcases=1
is_ended=False
command=input()
while command!="End":
    current_load=float(command)
    if suitcases%3==0:
        current_load*=1.1
    taken_space+=current_load
    if taken_space>trunk_capacity:
        is_ended=True
        break
    suitcases+=1
    command = input()
if command=="End":
    print("Congratulations! All suitcases are loaded!")
if trunk_capacity<taken_space:
    print("No more space!")
print(f"Statistic: {suitcases-1} suitcases loaded.")

