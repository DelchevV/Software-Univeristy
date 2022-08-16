day=input()
is_weekend= day=="Sunday" or day=="Saturday"
is_workday= day=="Monday" or day=="Monday" or day=="Tuesday" or day=="Wednesday" or day=="Thursday" or day=="Friday"

if is_workday:
    print("Working day")
elif is_weekend:
    print("Weekend")
else:
    print("Error")