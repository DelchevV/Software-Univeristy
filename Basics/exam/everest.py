start=5364
end=8848
days=1
is_reached=False
command=input()
while command!="END":
    if command=="Yes":
        days+=1
    if days>5:
        break
    current_distance=int(input())
    start+=current_distance
    if start>=end:
        is_reached=True
        break

    command=input()
if is_reached:
    print(f"Goal reached for {days} days!")
else:
    print("Failed!")
    print(f"{start}")