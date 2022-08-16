v=int(input())
p1=int(input())
p2=int(input())
h=int(input())

water_from_p1=p1*h
water_from_p2=p2*h
current_water_in_pool=water_from_p1+water_from_p2
in_percents= v/1-current_water_in_pool/1
print(f"The pool is {in_percents}% full.")