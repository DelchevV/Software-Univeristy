file='text.txt'
try:
    with open(f'sources/{file}') as text:
        print('File Found')
except FileNotFoundError:
    print('File not found')
