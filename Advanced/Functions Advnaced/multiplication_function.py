def multiply(*kwargs):
    result=1
    for num in kwargs:
        result*=num
    return result

print(multiply(4, 5, 6, 1, 3))