path_input=input().split("\\")

last_path=path_input[-1]
split_by_name_and_ext=last_path.split(".")
name=split_by_name_and_ext[0]
extension=split_by_name_and_ext[1]

print(f"File name: {name}\n"
      f"File extension: {extension}")