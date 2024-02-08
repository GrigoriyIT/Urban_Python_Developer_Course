from pprint import pprint


file_name = '09_File_opening_modes.txt'
file = open(file_name, mode='r', encoding='utf8')
file_content = file.read()
file.close()
pprint(file_content)