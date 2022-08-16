joinery_count=int(input())
type_of_joinery=input()
type_of_delivery=input()
s90x130=110
s100x150=140
s130x180=190
s200x300=250
delivery=0
price=0
if joinery_count<10:
    print("Invalid order")
    exit()
if type_of_joinery=="90X130":
    if joinery_count>60:
        s90x130*=0.92
    elif joinery_count>30:
        s90x130*=0.95
    price = joinery_count * s90x130
elif type_of_joinery=="100X150":
    if joinery_count>80:
        s100x150*=0.90
    elif joinery_count>40:
        s100x150*=0.94
    price = joinery_count * s100x150
elif type_of_joinery=="130X180":
    if joinery_count>50:
        s130x180*=0.88
    elif joinery_count>20:
        s130x180*=0.93
    price = joinery_count*s130x180
elif type_of_joinery=="200X300":
    if joinery_count>50:
        s200x300*=0.86
    elif joinery_count>25:
        s200x300*=0.91
    price=joinery_count*s200x300

if type_of_delivery=="With delivery":
    delivery=60
price+=delivery
if joinery_count>99:
    price*=0.96
print(f"{price:.2f} BGN")