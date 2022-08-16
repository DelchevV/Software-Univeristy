# You will be receiving to-do notes until you get the command "End". The notes will be in the format: "{importance}-{note}".
# Return a list containing all to-do notes sorted by importance in ascending order.
# The importance value will always be an integer between 1 and 10 (inclusive).
tasks=[]
while True:
    to_do=input().split("-")
    if to_do[0]=="End":
        break
    priority=int(to_do[0])
    task=to_do[-1]
    tasks.append((priority,task))

ordered_tasks=[task_data[1] for task_data in sorted(tasks)]
print(ordered_tasks)

