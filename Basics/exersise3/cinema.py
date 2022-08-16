type_of_movie=input()
roll=int(input())
collumn=int(input())

places=roll*collumn
total=0
if type_of_movie=="Premiere":
    total=places*12.00
elif type_of_movie=="Normal":
    total=places*7.50
elif type_of_movie=="Discount":
    total=places*5.00

print(f"{total:.2f} leva")
