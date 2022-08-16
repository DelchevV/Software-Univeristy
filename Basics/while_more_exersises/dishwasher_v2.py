bottles=int(input())
detegrent_in_ml=bottles*750
used_detegredent=0
pots=0
dishes=0
counter=1
command=input()
while detegrent_in_ml>=used_detegredent:
    if command=="End":
        break
    if counter%3==0:
        pots+=int(command)
        used_detegredent+=int(command)*15
    else:
        dishes+=int(command)
        used_detegredent+=int(command)*5
    counter+=1
    if used_detegredent > detegrent_in_ml:
        break
    command=input()
diffrence=abs(detegrent_in_ml-used_detegredent)
if used_detegredent>detegrent_in_ml:
    print(f"Not enough detergent, {diffrence} ml. more necessary!")
else:
    print("Detergent was enough!")
    print(f"{dishes} dishes and {pots} pots were washed.")
    print(f"Leftover detergent {diffrence} ml.")