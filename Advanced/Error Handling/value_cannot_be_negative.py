class ValueCannotBeNegative(Exception):
    pass


nums = []
for i in range(5):
    num = int(input())
    if num<0:
        raise ValueCannotBeNegative
    else:
        nums.append(num)