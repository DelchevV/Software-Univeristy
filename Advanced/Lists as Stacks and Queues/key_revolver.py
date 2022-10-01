from collections import deque
price_per_bullet=int(input())
size_of_barrel=int(input())
bullets=[int(_) for _ in input().split(" ")]
lockers=[int(_) for _ in input().split(" ")]
lockers=deque(lockers)
intelligence_value=int(input())
out_of_money=False
out_of_ammo=False
total_shots=0
shots_per_barrel=0
while lockers:
    total_shots+=1
    shots_per_barrel+=1
    if bullets:

        bullet=bullets.pop()
    else:
        out_of_ammo=True
        break
    if bullet<=lockers[0]:
        lockers.popleft()
        print('Bang!')
    else:
        print('Ping!')
    if bullets:
        if shots_per_barrel==size_of_barrel:
            if intelligence_value-(total_shots*price_per_bullet)<0:
                out_of_money=True
                break
            else:
                print("Reloading!")
                shots_per_barrel=0
    else:
        out_of_ammo=True
        break

money_for_bullets=total_shots*price_per_bullet
profit=intelligence_value-money_for_bullets
if not out_of_money and   len(lockers)<=0:
    print(f'{len(bullets)} bullets left. Earned ${profit}')
else:
    print(f"Couldn't get through. Locks left: {len(lockers)}")




