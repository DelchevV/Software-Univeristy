# Write a program that helps you keep track of your shot targets. You will receive a sequence with integers, separated by a single space, representing targets and their value. Afterward, you will be receiving indices until the "End" command is given, and you need to print the targets and the count of shot targets.
# Every time you receive an index, you need to shoot the target on that index, if it is possible.
# Every time you shoot a target, its value becomes -1, and it is considered shot. Along with that, you also need to:
# •	Reduce all the other targets, which have greater values than your current target, with its value.
# •	Increase all the other targets, which have less than or equal value to the shot target, with its value.
# Keep in mind that you can't shoot a target, which is already shot. You also can't increase or reduce a target, which is considered shot.
# When you receive the "End" command, print the targets in their current state and the count of shot targets in the following format:
# "Shot targets: {count} -> {target1} {target2}… {targetn}"

nums=list(map(int, input().split()))
while True:
    command=input()
    if command=="End":
        break
    current_target_index=int(command)
    if current_target_index<len(nums):
        current_number = nums[current_target_index]
        nums[current_target_index]=-1
    else:
        continue
    for target in range(len(nums)):
        if nums[target]!=-1:
            if nums[target]>current_number:
                nums[target]-=current_number
            elif nums[target]<=current_number:
                nums[target]+=current_number
made_shots=0
for item in nums:
    if item==-1:
        made_shots+=1
string_nums=list(str(st) for st in nums)
print(f'Shot targets: {made_shots} -> {" ".join(string_nums)}')

