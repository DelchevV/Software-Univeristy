def add_func(models,phones):
    if models not in phones:
        phones.append(models)
    return phones


def remove_func(models,phones):
    if models in phones:
        phones.remove(models)
    return phones


def bonus_func(old,new,phones):
    if old in phones:
        index_of_old=phones.index(old)
        phones.insert(index_of_old+1,new)
    return phones


def last_func(models,phones):
    if models in phones:
        index_of_model=phones.index(models)
        phones.pop(index_of_model)
        phones.append(models)
    return phones


phone=input().split(", ")
while True:
    data=input().split(" - ")
    command=data[0]
    if command=="End":
        print(", ".join(phone))
        break
    model=data[1]
    if command=="Add":
        phone=add_func(model,phone)
    elif command=="Remove":
        phone=remove_func(model,phone)
    elif command=="Bonus phone":
        old_and_new=model.split(":")
        old_model=old_and_new[0]
        new_model=old_and_new[1]
        phone=bonus_func(old_model,new_model,phone)
    elif command=="Last":
        phone=last_func(model,phone)
