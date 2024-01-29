import os

def rename_files(directory_path, file_extension):

    if not os.path.exists(directory):
        print(f"Directory '{directory}' ไม่พบ")
        return

files = [file for file in os.listdir(directory) if file.endswith(file_extension)]


files_to_rename.sort()

for index, file_name in enumerate(files_to_rename, start=1):
    new_name = f"{index:03d}"
    os.rename(file_name, new_name)     
    print(f"Renamed {file_name} to {new_name}")

directory_path = "D:/Job-04--Batch-Rename_6620301001"  
file_extension = ".jpg"
rename_files(directory_path, file_extension)
