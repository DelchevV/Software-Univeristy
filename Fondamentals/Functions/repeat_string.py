def repeat_string_func(text,repeater):
    result=text*repeater
    return result


input_text=input()
input_repeater=int(input())
print(repeat_string_func(input_text,input_repeater))