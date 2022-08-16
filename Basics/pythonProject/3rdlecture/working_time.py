hour= int(input())
day=input()
is_workday= day=="Monday" or day=="Monday" or day=="Tuesday" or day=="Wednesday" or day=="Thursday" or day=="Friday" or day=="Saturday"
is_hour= hour>=10 and hour<=18

if is_hour and is_workday:
    print("open")
else:
    print("closed")