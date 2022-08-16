def round_func(nums):
    rounded_list=[round(num) for num in nums]
    return  rounded_list


numbers=list(map(float, input().split(" ")))
print(round_func(numbers))
