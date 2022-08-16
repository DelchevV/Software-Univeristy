period=int(input())
doctors=7
checked=0
unchecked=0

for i in range(1,period+1):
    if i%3==0 and checked<unchecked:
        doctors += 1
    patients = int(input())
    if doctors>=patients:
        checked+=patients
    else:
        unchecked+=patients-doctors
        checked+=doctors

print(f"Treated patients: {checked}.")
print(f"Untreated patients: {unchecked}.")

