def sorting_cheeses(**kwargs):
    result=sorted(kwargs.items(), key=lambda x: (-len(x[1]),x[0]))
    result_str=''
    for key, value in result:
        sorted_values=sorted(value,reverse=True)
        result_str+=key +'\n'
        result_str+="\n".join(map(str,sorted_values))+'\n'
    return result_str



print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
