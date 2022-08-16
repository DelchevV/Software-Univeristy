budget=int(input())
is_overdraft=False
command=input()

while command!="End":
    budget-=int(command)
    if budget<0:
        is_overdraft=True
        break
    command=input()
if is_overdraft==True:
    print("You went in overdraft!")
else:
    print("You bought everything needed.")
