command=input()
saved_money=0
while command!="End":
    needed_money=float(input())
    while needed_money>saved_money:
        current_money=float(input())
        saved_money+=current_money
    print(f"Going to {command}!")
    saved_money=0
    command = input()
    if command=="End":
        break