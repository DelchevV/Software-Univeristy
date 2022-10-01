def even_odd_filter(**kwargs):
    result={}
    for key,value in kwargs.items():
        if key=="even":
            kwargs[key]=[num for num in value if num%2==0]
        elif key=="odd":
            kwargs[key]=[num for num in value if num%2!=0]

    result=sorted(kwargs.items(), key=lambda x: -len(x[1]))
    final_dict={}
    for s in result:
        final_dict[s[0]]=s[1]
    return final_dict





print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))



