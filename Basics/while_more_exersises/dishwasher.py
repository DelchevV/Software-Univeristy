bottles_of_detegrent=int(input())
nedeed_detegredent=0
ml_of_detegredent=bottles_of_detegrent*750
detegrent_for_dishes=0
detegrent_for_pots=0
reload=0
dishes=0
pots=0
command=input()
while command!="End":
    reload+=1
    if reload%3==0:
        pots+=int(command)
    else:
        dishes+=int(command)
    nedeed_detegredent += pots*15 + dishes*5
    if nedeed_detegredent>ml_of_detegredent:
        break
    command = input()

diffrence=abs(ml_of_detegredent-nedeed_detegredent)
if ml_of_detegredent>=nedeed_detegredent:
    print(f"Detergent was enough!")
    print(f"{dishes} dishes and {pots} pots were washed.")
    print(f"Leftover detergent {diffrence} ml.")
else:
    print(f"Not enough detergent, {diffrence} ml. more necessary!")