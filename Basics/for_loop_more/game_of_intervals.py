rounds=int(input())
from_0_to_9=0
from_10_to_19=0
from_20_to_29=0
from_30_to_39=0
from_40_to_50=0
invalid_number=0
total=0
for i in range(rounds):
    number=int(input())
    if  number>=0 and number<=50:
        if number<=9:
            total+=number*0.2
            from_0_to_9+=1
        elif number<=19:
            total +=number* 0.3
            from_10_to_19+=1
        elif number<=29:
            total +=number* 0.4
            from_20_to_29+=1
        elif number<=39:
            total+=50
            from_30_to_39+=1
        elif number<=50:
            total+=100
            from_40_to_50+=1
    else:
        total/=2
        invalid_number+=1

print(f"{total:.2f}")
print(f"From 0 to 9: {from_0_to_9/rounds*100:.2f}%")
print(f"From 10 to 19: {from_10_to_19/rounds*100:.2f}%")
print(f"From 20 to 29: {from_20_to_29/rounds*100:.2f}%")
print(f"From 30 to 39: {from_30_to_39/rounds*100:.2f}%")
print(f"From 40 to 50: {from_40_to_50/rounds*100:.2f}%")
print(f"Invalid numbers: {invalid_number/rounds*100:.2f}%")