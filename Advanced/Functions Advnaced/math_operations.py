def math_operations(*args, **kwargs):
    is_out_of_nums = False
    numbers = list(args)
    while numbers:
        for key in kwargs:
            if len(numbers) == 0:
                is_out_of_nums = True
                break
            current_num = numbers.pop(0)
            if key == 'd':
                if current_num != 0:
                    kwargs[key] /= current_num
            elif key == "s":
                kwargs[key] -= current_num
            elif key == "a":
                kwargs[key] += current_num
            elif key == "m":
                kwargs[key] *= current_num
        if is_out_of_nums:
            break
    result = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
    output = ''
    for res in result:
        output += f'{res[0]}: {res[1]:.1f}\n'
    return output


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))
