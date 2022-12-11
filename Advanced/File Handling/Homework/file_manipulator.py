import os


def create_func(name):
    with open(f'sources/{name}', 'w') as writer:
        writer.write("")
    return


def add_func(name, contents):
    with open(f'sources/{name}', 'a') as writer:
        writer.write(contents + '\n')
    return


def replace_func(name, old, new):
    try:
        with open(f"sources/{name}", 'r') as file:
            text = file.readlines()
            for row in range(len(text)):
                text[row] = text[row].replace(old, new)

        with open(f"sources/{name}", 'w') as file:
            for line in text:
                file.write(line)

    except FileNotFoundError:
        print("An error occurred")
    return


def delete_func(name):
    try:
        os.remove(f'sources/{name}')
    except FileNotFoundError:
        print("An error occurred")

    return


while True:
    entry = input()
    if entry == 'End':
        break

    entry = entry.split('-')
    command = entry[0]
    file_name = entry[1]

    if command == "Add":
        content = entry[2]
        add_func(file_name, content)
    elif command == 'Create':
        create_func(file_name)
    elif command == 'Replace':
        old_str = entry[2]
        new_str = entry[3]
        replace_func(file_name, old_str, new_str)
    elif command == "Delete":
        delete_func(file_name)
