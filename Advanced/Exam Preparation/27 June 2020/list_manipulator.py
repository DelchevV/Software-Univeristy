from collections import deque


def list_manipulator(nums, *args):
    nums = deque(nums)

    if args[0] == "add" and args[1] == "beginning":
        for index in range(len(args) - 1, 1, -1):
            nums.appendleft(args[index])

    elif args[0] == 'add' and args[1] == "end":
        for index in range(2,len(args)):
            nums.append(args[index])

    elif args[0] == 'remove' and args[1] == "beginning":
        if len(args)>2:
            for _ in range(args[2]):
                if nums:
                    nums.popleft()
        else:
            nums.popleft()

    elif args[0] == "remove" and args[1] == "end":
        if len(args) > 2:
            for _ in range(args[2]):
                if nums:
                    nums.pop()
        else:
            nums.pop()

    return list(nums)

print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))

