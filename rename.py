import os

def rename_files(directory_path, file_extension):

    if not os.path.exists(directory):
        print(f"Directory '{directory}' ไม่พบ")
        return

files = [file for file in os.listdir(directory) if file.endswith(file_extension)]


files.sort()

for i, file in enumerate(files, start=1):

    new_name = f"{i:03d}{file_extension}"

    old_path = os.path.join(directory, file)
    ew_path = os.path.join(directory, new_name)

    os.rename(old_path, new_path)
    print(f"Rename: {file} = {new_name}")


directory_path = "D:/Job-04--Batch-Rename_6620301001"  
file_extension = ".jpg"
rename_files(directory_path, file_extension)
