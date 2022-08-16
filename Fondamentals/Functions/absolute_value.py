def abs_fun(nums):
    result=[abs(num) for num in nums]
    return result


numbers=list(map(float,input().split(" ")))
print(abs_fun(numbers))
