voucher_price=int(input())
command=input()
money=0
ticket=0
other_thing=0
while command!="End":

    if len(command)>8:
        money+=ord(command[0])+ord(command[1])
        ticket+=1
        if money > voucher_price:
            ticket-=1
            break

    else:
        money += ord(command[0])
        other_thing+=1
        if money > voucher_price:
            other_thing-=1
            break

    command = input()
print(f"{ticket}")
print(f"{other_thing}")


