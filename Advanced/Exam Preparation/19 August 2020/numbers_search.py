import sys


def find_max_min(args):
    smallest = sys.maxsize
    biggest = -sys.maxsize

    for num in args:
        if num < smallest:
            smallest = num
        if num > biggest:
            biggest = num

    return smallest, biggest


def check_for_dup(args):
    new_list = []
    dup_list = []

    for num in args:
        if num not in new_list:
            new_list.append(num)
        else:
            dup_list.append(num)

    return dup_list


def find_missing_num(min_n, max_n, args):
    missing_n = 0

    for missing in range(min_n, max_n + 1):
        if missing not in args:
            missing_n = missing

    return missing_n


def numbers_searching(*args):
    min_num, max_num = find_max_min(args)

    duplicates = check_for_dup(args)

    missing_num = find_missing_num(min_num, max_num, args)

    return [missing_num, sorted((set(duplicates)), key=lambda x: x)]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
