def palindrome_func(list_of_ints):
    for integer in list(list_of_ints):
        palindrome_list = []
        number = integer
        revs_number = 0

        while number > 0:
            # Logic
            remainder = number % 10
            revs_number = (revs_number * 10) + remainder
            number = number // 10
        if revs_number == integer:
            print("True")
        else:
            print("False")


list_of_strings = input().split(", ")
list_of_ints = []
for item in list_of_strings:
    list_of_ints.append(int(item))
palindrome_func(list_of_ints)
