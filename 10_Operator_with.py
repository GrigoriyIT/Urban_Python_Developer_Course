file_name = '09_File_opening_modes.txt'
with open(file_name, mode='r', encoding='utf8') as file:
    file_content = file.read()
print(file_content)
