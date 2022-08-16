x=float(input())
y=float(input())
z=float(input())
percent=float(input())/100

v=x*y*z/1000
occupied=v*percent
needed_water=v-occupied
print(needed_water)
