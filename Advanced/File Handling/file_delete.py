import os

file_name = 'file_to_delete'
try:
    os.remove(f"sources/{file_name}")
except FileNotFoundError:
    print('File does not exists')
