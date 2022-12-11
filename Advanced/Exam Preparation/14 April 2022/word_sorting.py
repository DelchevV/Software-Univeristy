def words_sorting(*args):
    words_dict = {}

    for word in args:
        ch_sum = 0

        for ch in word:
            ch_sum += ord(ch)
        words_dict[word] = ch_sum

    final_print = ''
    is_even = False
    sum_of_all_vals = 0

    for val in words_dict.values():
        sum_of_all_vals += val

    if sum_of_all_vals % 2 != 0:
        result = sorted(words_dict.items(), key=lambda x: -x[1])
    else:
        result = sorted(words_dict.items(), key=lambda x: x[0])

    for res in result:
        final_print += f'{res[0]} - {res[1]}\n'
    return final_print


print(
    words_sorting(
        'cacophony',
        'accolade'
    ))
