import os
# report.txt file will be created after running the program
# 'sources\Example'    for input
directory = r'sources\Example'
extensions = {}

# reading only the files in the directory
for filename in os.listdir(directory):
    file = os.path.join(directory, filename)
    if "." in filename:
        extension = filename.split(".")[-1]

        # adds extension and it's files into a dict
        if extension not in extensions:
            extensions[extension] = []
        extensions[extension].append(filename)

# create a report.txt file with the result
with open('sources/report.txt', 'w') as writer:

    # sorting by extensions
    extensions = sorted(extensions.items(), key=lambda x: x[0])
    for extension, file_name in extensions:
        writer.write(f'.{extension}\n')

        # sorting by file names
        for file in sorted(file_name, key=lambda x: x):
            writer.write(f'- - - {file}\n')
