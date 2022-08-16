lines_of_text=int(input())
result={}
for line in range(lines_of_text):
    text=input()
    start_name=text.index("@")
    end_name=text.index("|")

    start_age = text.index("#")
    end_age = text.index("*")

    name=text[start_name+1:end_name]
    age=text[start_age+1:end_age]
    result[name]=int(age)
for name,age in result.items():
    print(f"{name} is {age} years old.")