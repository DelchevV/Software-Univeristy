lines=int(input())
cars=set()
for line in range(lines):
    state, plate=input().split(", ")
    if state=="IN":
        cars.add(plate)
    if state=="OUT":
        cars.discard(plate)
if cars:
    for car in cars:
        print(car)
else:
    print('Parking Lot is Empty')