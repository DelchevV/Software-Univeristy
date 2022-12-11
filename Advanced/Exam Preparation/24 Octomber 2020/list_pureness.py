from collections import deque


def best_list_pureness(*args):

    results = {}
    nums = deque(args[0])
    current_res = 0
    index = 0

    for idx in range(len(nums)):
        current_res += nums[idx] * idx

    results[f"{index}"] = current_res

    for rotation in range(args[-1]):
        nums.appendleft(nums.pop())
        current_res = 0

        for idx in range(len(nums)):
            current_res += nums[idx] * idx
        index += 1
        results[f'{index}'] = current_res

    for key, value in sorted(results.items(), key=lambda x: (-x[1], int(x[0]))):
        return f"Best pureness {value} after {key} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
