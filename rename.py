import os

def rename_files(directory_path, file_extension):

os.chdir(directory_path)

files_to_rename = [file for file in os.listdir() if file.endswith(file_extension)]


files_to_rename.sort()

for index, file_name in enumerate(files_to_rename, start=1):
new_name = f"{index:03d}{file_extension}"
       