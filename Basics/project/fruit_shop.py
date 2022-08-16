fruit=input()
day=input()
quantity=float(input())
price=0
is_valid = True

is_working_day= day=="Monday" or day=="Tuesday" or day=="Wednesday" or day=="Thursday" or day=="Friday"
is_weekend= day=="Saturday" or day=="Sunday"

if is_working_day:
    if fruit=="banana":
        price= quantity*2.50
    elif fruit=="apple":
        price=quantity*1.20
    elif fruit=="orange":
        price = quantity * 0.85
    elif fruit=="grapefruit":
        price = quantity * 1.45
    elif fruit=="kiwi":
        price = quantity * 2.70
    elif fruit=="pineapple":
        price = quantity * 5.50
    elif fruit=="grapes":
        price = quantity * 3.85
    else:
        is_valid=False
elif is_weekend:
    if fruit=="banana":
        price= quantity*2.70
    elif fruit=="apple":
        price=quantity*1.25
    elif fruit=="orange":
        price = quantity * 0.90
    elif fruit=="grapefruit":
        price = quantity * 1.60
    elif fruit=="kiwi":
        price = quantity * 3.00
    elif fruit=="pineapple":
        price = quantity * 5.60
    elif fruit=="grapes":
        price = quantity * 4.20
    else:
        is_valid=False
else:
    is_valid = False
if is_valid==True:
    print(f"{price:.2f}")
else:
    print("error")
