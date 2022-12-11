def naughty_or_nice_list(kids, *args, **kwargs):
    naughty_nums, nice_nums = separation(args)
    good_kids = []
    bad_kids = []
    none_type_kids = []
    copy_of_kids=kids.copy()
    for kid in copy_of_kids:
        current_num, current_name = kid
        same_name = 0
        for kido in kids:
            if current_num == kido[0]:
                same_name += 1

        if same_name == 1:
            if current_num in naughty_nums:
                bad_kids.append(current_name)
                kids.remove(kid)
            elif current_num in nice_nums:
                good_kids.append(current_name)
                kids.remove(kid)

    copy_of_kids=kids.copy()

    for key, value in kwargs.items():
        same_name = 0
        for kid in copy_of_kids:
            if key == kid[1]:
                same_name += 1
        if same_name == 1:
            if value == "Naughty":
                bad_kids.append(key)

            elif value == "Nice":
                good_kids.append(key)




    result = ''
    if good_kids:
        result += f'Nice: {", ".join(good_kids)}' + '\n'
    if bad_kids:
        result += f'Naughty: {", ".join(bad_kids)}' + '\n'
    if none_type_kids:
        result += f'Not found: {", ".join(none_type_kids)}'
    return result


def separation(args):
    naughty_num = []
    nice_num = []
    for el in args:
        text = el.split('-')
        if text[-1] == 'Naughty':
            naughty_num.append(int(text[0]))
        elif text[-1] == "Nice":
            nice_num.append(int(text[0]))
    return naughty_num, nice_num


print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
print()
print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))
print()
print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))
