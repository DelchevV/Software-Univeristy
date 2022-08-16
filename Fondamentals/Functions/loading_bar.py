def loading_bar(percent):
    signs = 0
    dots = 0
    loading_bar_list = []
    signs = int(percent / 10)
    dots = 10 - signs
    for item_sign in range(signs):
        loading_bar_list.append("%")
    for item_dot in range(dots):
        loading_bar_list.append(".")
    final_string = "["
    final_string += "".join(map(str, loading_bar_list))
    final_string += "]"
    if percent == 100:
        print(f"{percent}% Complete!")
        print(final_string)
    else:
        print(f"{percent}% {final_string}")
        print("Still loading...")


number = int(input())
loading_bar(number)
