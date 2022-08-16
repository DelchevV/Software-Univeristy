def is_valid_pass(password_input):
    digits = 0
    is_invalid_input = False
    length = False
    if 6 <= len(password_input) <= 10:
        length = True
    for item in range(len(password_input)):
        var_digit = False
        var_letter = False
        current_item = password_input[item]
        var_digit = current_item.isdigit()
        var_letter = current_item.isalpha()
        if var_digit or var_letter:
            if var_digit:
                digits += 1
        else:
            is_invalid_input = True
    if not is_invalid_input:
        if digits >= 2:
            if length:
                print("Password is valid")
    if not length:
        print("Password must be between 6 and 10 characters")
    if is_invalid_input:
        print("Password must consist only of letters and digits")
    if digits < 2:
        print("Password must have at least 2 digits")


password = input()
is_valid_pass(password)
