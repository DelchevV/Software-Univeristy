def string_betweem(start,end):
    result=""
    for string in range(start+1,end):
        result+=chr(string)+ " "
    return result


start_of_string=ord(input())
end_of_string=ord(input())


print(string_betweem(start_of_string,end_of_string))