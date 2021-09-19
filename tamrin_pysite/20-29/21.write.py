with open('file_to_save.txt', 'w') as open_file:
    open_file.write('A string to write 234')

with open("file_to_save.txt", "r") as openf:
    openf.read()