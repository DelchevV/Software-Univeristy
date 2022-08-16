actor_name=input()
total_points=float(input())
examinators=int(input())

for number in range(examinators):
    current_name=input()
    current_points=float(input())
    current_final_points= len(current_name)*current_points/2
    total_points+=current_final_points
    if total_points>1250.5:

        break
if total_points > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
else:
    diffrence=1250.5-total_points
    print(f"Sorry, {actor_name} you need {diffrence:.1f} more!")